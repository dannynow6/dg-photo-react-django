from django.contrib import admin
from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list = ("title", "camera_make", "format")

    admin.site.register(Photo)
