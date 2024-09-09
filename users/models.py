# users/models.py

from django.contrib.auth.models import User
from django.db import models

# Se desejar estender o modelo User, descomente o código abaixo
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Adicione campos adicionais se necessário
#
#     def __str__(self):
#         return self.user.username
