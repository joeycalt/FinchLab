from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Dog, Toy, Favorite
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class DogsList(TemplateView):
    template_name = "dogs_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        print(name)
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name)
            context['header'] = f"Searching through Dogs list for {name}"
        else:
            context["dogs"] = Dog.objects.filter(user=self.request.user)
            context['header'] = 'All Dogs'
        return context

@method_decorator(login_required, name='dispatch')
class DogForm(CreateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'purebred', 'crossbreed']
    template_name = "dog_form.html"
    success_url = "/dogs/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DogForm, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'purebred', 'crossbreed']
    template_name = "dog_update.html"
    success_url = "/dogs/"

    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class DogDelete(DeleteView):
    model = Dog
    template_name = "dog_delete.html"
    success_url = "/dogs/"

@method_decorator(login_required, name='dispatch')
class ToyCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        img = request.POST.get("img")
        dog = Dog.objects.get(pk=pk)
        Toy.objects.create(title=title, img=img, doggo=dog)
        return redirect('dog_detail', pk=pk)

@method_decorator(login_required, name='dispatch')
class FavoriteListAssoc(View):

    def get(self, request, pk, toy_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Favorite.objects.get(pk=pk).toys.remove(toy_pk)
        if assoc == "add":
            Favorite.objects.get(pk=pk).toys.add(toy_pk)
        return redirect('home')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dogs_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
