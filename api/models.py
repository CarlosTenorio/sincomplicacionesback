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
# User Province
##################################################################
class Province(models.Model):
    name = models.CharField(max_length=128, null=True,
                            blank=True, verbose_name='Nombre')

    lat = models.FloatField(null=True, blank=True, verbose_name='Latitud')
    lng = models.FloatField(null=True, blank=True, verbose_name='Longitud')

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificación')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name="countries",
                                verbose_name='País', null=True, blank=True)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.name


##################################################################
# User City
##################################################################
class City(models.Model):
    name = models.CharField(max_length=128, null=True,
                            blank=True, verbose_name='Nombre')

    lat = models.FloatField(null=True, blank=True, verbose_name='Latitud')
    lng = models.FloatField(null=True, blank=True, verbose_name='Longitud')

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificación')

    province = models.ForeignKey(Province, on_delete=models.SET_NULL, related_name="provinces",
                                 verbose_name='Provincia', null=True, blank=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name


##################################################################
# City Postal Code
##################################################################
class PostalCode(models.Model):
    code = models.IntegerField(null=True, blank=True, verbose_name='Código')

    city = models.ForeignKey(
        City, related_name='city_postal', verbose_name='Ciudad', null=True, blank=True)

    class Meta:
        verbose_name = 'Código Postal'
        verbose_name_plural = 'Codigos Potales'

    def __str__(self):
        return "{}".format(self.code)


##################################################################
# User Extended of Django User
##################################################################
class UserExtended(models.Model):
    GENRE_CHOICES = (
        (0, 'MALE'),
        (1, 'FEMALE')
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_extended')
    height = models.FloatField(null=True, blank=True, verbose_name='Altura')
    scoreTotal = models.FloatField(
        null=True, blank=True, verbose_name='Puntuación total')
    genre = models.IntegerField(
        null=True, blank=True, verbose_name='Género', default=0, choices=GENRE_CHOICES)
    like = models.IntegerField(
        null=True, blank=True, verbose_name='Le gusta', default=1, choices=GENRE_CHOICES)

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    city = models.ForeignKey(
        City, related_name='city_user', verbose_name='Ciudad', null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.user.username


##################################################################
# User Extended Profile
##################################################################
class UserProfile(models.Model):

    user_extended = models.OneToOneField(
        UserExtended, on_delete=models.CASCADE, blank=True, null=True,  related_name='user_profile')
    profile_photo = models.ImageField(
        upload_to='profiles/', blank=True, null=True)

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Perfil de profesional'
        verbose_name_plural = 'Perfiles de profesionales'

    def __str__(self):
        return self.professional.user.username


##################################################################
# Categories
##################################################################
class Category(models.Model):

    title = models.CharField(max_length=128, null=True,
                             blank=True, verbose_name='Título')
    description = models.CharField(
        null=True, blank=True, max_length=512, verbose_name='Descripción')

    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.title


##################################################################
# Photos os Users
##################################################################
class UserPhoto(models.Model):
    image = models.ImageField(
        upload_to="profesional_photos/", blank=True, null=True)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificación')

    user = models.ForeignKey(UserExtended, related_name='user_photo',
                             verbose_name='Usuario', null=True, blank=True)

    class Meta:
        verbose_name = 'Foto del usuario'
        verbose_name_plural = 'Fotos de los usuarios'

    def __str__(self):
        return "{}".format(self.id)
