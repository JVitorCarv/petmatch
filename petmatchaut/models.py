from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.
class ProfileInfo(AbstractBaseUser):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=12, blank=True)
    date_joined = models.DateTimeField()
