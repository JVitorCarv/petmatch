from email.policy import default
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse                                                                                            

'''
# Create your models here.
class ProfileInfo(AbstractBaseUser):
    person = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    cpf = models.CharField(max_length=12, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.person}' 
'''

class pet_perfil(models.Model):
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=30, default="your pet name")
    race = models.CharField(max_length=30)
    pet_age = models.CharField(max_length=3)
    pet_image = models.ImageField(default="default.jpg", upload_to="pet_pics")
    
    def __str__(self):
        return self.pet_name + '|' + str(self.owner)

    def get_absolute_url(self):
        return reverse("profile")
    
'''
    @receiver(post_save, sender=User)
    def create_pet_perfil(sender, instance, created, **kwargs):
        if created:
            pet_perfil.objects.create(user=instance)

    
    @receiver(post_save, sender=User)
    def salvar_perfil(sender, instance, **kwargs):
        instance.save()
    '''
        