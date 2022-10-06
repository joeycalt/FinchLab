from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Dog(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=250, null='True')
    bio = models.TextField(max_length=500)
    purebred = models.BooleanField(default=False)
    crossbreed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Toy(models.Model):

    title = models.CharField(max_length=150)
    img = models.CharField(max_length=250, null='True')
    doggo = models.ForeignKey(
        Dog, on_delete=models.CASCADE, related_name="toys", null="True")

    def __str__(self):
        return self.title

class Favorite(models.Model):

    title = models.CharField(max_length=150)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.title