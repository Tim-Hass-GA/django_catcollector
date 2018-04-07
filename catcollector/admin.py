from django.contrib import admin
from . models import Cat
# Register your models here.
# allows us to use cat on admin panel
admin.site.register(Cat)
