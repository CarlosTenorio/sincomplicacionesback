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

    image = models.ImageField(
        upload_to="country_photos/", blank=True, null=True, verbose_name='Imagen')

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
# Shipping
##################################################################
class Shipping(models.Model):
    SHIPPING_TYPE = (
        (0, 'PURCHASE'),
        (1, 'SALE')
    )

    date = models.DateField(verbose_name='Fecha del envío')

    shipping_type = models.IntegerField(null=True, blank=True,
        verbose_name='Tipo', default=0, choices=SHIPPING_TYPE)

    shipping_costs = models.FloatField(null=True, blank=True, verbose_name='Latitud')

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Envío'
        verbose_name_plural = 'Envíos'

    def __str__(self):
        return self.date


##################################################################
# Card
##################################################################
class Card(models.Model):

    title = models.CharField(max_length=128, null=True,
                             blank=True, verbose_name='Carta')
    description = models.CharField(
        null=True, blank=True, max_length=512, verbose_name='Descripción')

    price = models.FloatField(null=True, blank=True, verbose_name='Precio')

    image = models.ImageField(
        upload_to="card_photos/", blank=True, null=True, verbose_name='Imagen')

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
        related_name="country_card", verbose_name='País', null=True, blank=True)

    shipping = models.ForeignKey(Shipping, on_delete=models.SET_NULL,
        related_name="shipping_card", verbose_name='Envío', null=True, blank=True)

    class Meta:
        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'

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
