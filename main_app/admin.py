from django.contrib import admin
from .models import Dog, Toy, Favorite
# Register your models here.
admin.site.register(Dog)
admin.site.register(Toy)
admin.site.register(Favorite)

