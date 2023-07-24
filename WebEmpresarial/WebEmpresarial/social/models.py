from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    font_awesome = models.CharField(max_length=75, verbose_name='Font-awesome', default='fa-') 
    created = models.DateTimeField(verbose_name="Fecha Creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha Edicion", auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["-created"]

    def __str__(self):
        return self.name