from django.conf import settings
from django.db import models
from users.models import CustomerUser
from products.models import Product
# Create your models here.


class Cart(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')

    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Carf of {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in cart of {self.cart.user.username}'