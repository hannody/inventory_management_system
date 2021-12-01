import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Supplier(models.Model):
    """
    Supplier model
    """

    class SupplierCategory(models.TextChoices):
        INTERNATIONAL = 'I', _('International')
        LOCAL = 'L', _('Local')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=False, null=False)
    address = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    category = models.CharField(
        max_length=len('International'),
        choices=SupplierCategory.choices,
        default=SupplierCategory.LOCAL,
        blank=False, null=False
    )

    def __str__(self):
        """
        String representation of the model (to return the name of the supplier)
        """
        return self.name


class Item(models.Model):
    """
    Item model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=256, blank=False, null=False)
    note = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0, blank=False, null=False)
    availability = models.BooleanField(default=False, blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    supplier = models.ForeignKey(max_length=128, to='Supplier', on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the model (to return the name of the item)
        """
        return self.name
