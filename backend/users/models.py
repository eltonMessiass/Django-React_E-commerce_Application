from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission



class CustomerUser(AbstractUser):
    groups =models.ManyToManyField(Group, related_name='customer_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customer_users', blank=True) 

from cart.models import Cart
@receiver(post_save, sender=CustomerUser)
def create_user_cart(sender, instance, created, **Kwargs):
    if created:
        Cart.objects.create(user=instance)

