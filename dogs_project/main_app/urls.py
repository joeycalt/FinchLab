from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dogs/', views.DogsList.as_view(), name="dogs_list"),
    path('dogs/new/', views.DogForm.as_view(), name="dog_form"),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name="dog_update"),
    path('dogs/<int:pk>/delete',views.DogDelete.as_view(), name="dog_delete"),
    path('dogs/<int:pk>/toys/new/', views.ToyCreate.as_view(), name="toy_create"),
    path('dogs/<int:pk>/toys/<int:toy_pk>/', views.FavoriteListAssoc.as_view(), name="favorite_list_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
