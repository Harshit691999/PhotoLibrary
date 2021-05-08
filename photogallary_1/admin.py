from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Photo)
# admin.site.register("model name")
# admin.site.register("model name")
# admin.site.register("model name")