# from email.policy import default
# from enum import unique
# from tabnanny import verbose
# from django.db import models
# from django.contrib import admin

# class Users(models.Model):
#     profile_image = models.ImageField(blank=False, default="", upload_to="images/users/")
#     name = models.CharField(max_length=500, null=False)
#     email = models.EmailField(max_length=500, null=False)
#     address = models.CharField(max_length=500, null=False)
#     phone = models.CharField(max_length=500, null=False)
#     password = models.CharField(max_length=500, null=False)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
