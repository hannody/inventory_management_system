from django.test import TestCase

from inventory.models import Item, Supplier


class InventoryTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier1', address='123 Main St.', category='L')
        self.item = Item.objects.create(name='Item 1', description='Item 1 description', stock=1200,
                                        supplier=Supplier.objects.first())

    def test_string_representation(self):
        self.assertEqual(str(self.supplier), self.supplier.name)
        self.assertEqual(str(self.item), self.item.name)