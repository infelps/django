# from django.db import models
#
#
# class Account(models.Model):
#     username = models.CharField(max_length=200)
#     password1 = models.TextField(max_length=200)
#     password2 = models.TextField(max_length=200)
#     job = models.TextField(max_length=200)

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     job = models.CharField(max_length=10, blank=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()