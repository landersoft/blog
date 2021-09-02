from django.contrib import admin
from blog.models import Perfil, Post , Tag

# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    model = Perfil

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "titulo",
        "subtitulo",
        "slug",
        "fecha_publicacion",
        "publicado",
    )

    list_filter = (
        "publicado",
        "fecha_publicacion",
    )

    list_editable = (
        "titulo",
        "subtitulo",
        "slug",
        "fecha_publicacion",
        "publicado",
    )

    search_fields = (
        "titulo",
        "subtitulo",
        "slug",
        "cuerpo"
    )

    prepopulated_fields = {
        "slug": (
            "titulo",
            "subtitulo",
        )
    }

    date_hierarchy = "fecha_publicacion"
    save_on_top = True