"""Registre dels models al panell d'administració de Django."""
from django.contrib import admin
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    """Configuració de la vista de Posts a l'admin."""

    list_display = ("title", "author", "date")
    list_filter = ("author", "tags", "date")
    # el slug es genera automàticament a partir del títol
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    """Configuració de la vista d'Autors a l'admin."""

    list_display = ("first_name", "last_name", "email")


class TagAdmin(admin.ModelAdmin):
    """Configuració de la vista de Tags a l'admin."""

    list_display = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
