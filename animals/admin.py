from django.contrib import admin
from animals.models import Animal

@admin.register(Animal)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ("kind", "description", "birthday", "image")
    search_fields = ("kind", "description")
    list_filter = ("birthday", "kind")