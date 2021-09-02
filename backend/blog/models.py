from django.db import models
from django.conf import settings
from django.utils import tree

# Create your models here.

class Perfil(models.Model):
    class Meta:
        verbose_name_plural = "Perfiles"
        
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ["-fecha_publicacion"]

    titulo = models.CharField(max_length=255, unique=True)
    subtitulo = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    cuerpo = models.TextField()
    meta_descripcion = models.CharField(max_length=150, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(default=False)
    publicado = models.BooleanField(default=False)


    autor = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)




