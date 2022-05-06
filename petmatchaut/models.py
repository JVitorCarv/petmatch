from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class ProfileInfo(AbstractBaseUser):
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cpf = models.CharField(max_length=12, blank=True)
    date_joined = models.DateTimeField()

class pet_perfil(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    pet_age = models.CharField(max_length=3)



    @receiver(post_save, sender=User)
    def create_pet_perfil(sender, instance, created, **kwargs):
        if created:
            pet_perfil.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def salvar_perfil(sender, instance, **kwargs):
        instance.perfil.save()
        