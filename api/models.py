from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(ModelBase):
    user = models.ForeignKey(User, related_name='locations')

    lat = models.DecimalField(max_digits=16, decimal_places=8)
    lng = models.DecimalField(max_digits=16, decimal_places=8)

    def __str__(self):
        return 'User {}: [{}, {}]'.format(self.user.pk, self.lat, self.lng)
