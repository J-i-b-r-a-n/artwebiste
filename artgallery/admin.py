from django.contrib import admin
from .models import Painting, Categories

# Register your models here.


class AdminPainting(admin.ModelAdmin):
    list_display = ['title', 'year', 'category']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Painting, AdminPainting)
admin.site.register(Categories)
