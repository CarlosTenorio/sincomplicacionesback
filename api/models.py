from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse


##################################################################
# User Country
##################################################################
class Country(models.Model):
    name = models.CharField(max_length=128, null=True,
                            blank=True, verbose_name='Nombre')

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


##################################################################
# Card
##################################################################
class Card(models.Model):

    title = models.CharField(max_length=128, null=True,
                             blank=True, verbose_name='Carta')
    description = models.CharField(
        null=True, blank=True, max_length=512, verbose_name='Descripción')

    image = models.ImageField(
        upload_to="card_photos/", blank=True, null=True, verbose_name='Imagen')

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
        related_name="country_card", verbose_name='País', null=True, blank=True)

    class Meta:
        verbose_name = 'Expansión'
        verbose_name_plural = 'Expansiones'

    def __str__(self):
        return self.title


##################################################################
# Expansion
##################################################################
class Expansion(models.Model):

    title = models.CharField(max_length=128, null=True,
                             blank=True, verbose_name='Título')

    image = models.ImageField(
        upload_to="expansion_photos/", blank=True, null=True, verbose_name='Imagen')

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Expansión'
        verbose_name_plural = 'Expansiones'

    def __str__(self):
        return self.title
