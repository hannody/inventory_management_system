from django.test import TestCase

from inventory.models import Item, Supplier


class InventoryTest(TestCase):
    """
    Test the inventory app Models (Item, Supplier)
    """

    def setUp(self):
        self.supplier1 = Supplier.objects.create(name='Supplier1', address='123 Main St.', category='L')
        self.supplier2 = Supplier.objects.create(name='Supplier2', address='456 Main St.', category='I')

        self.item = Item.objects.create(name='Item 1', description='Item 1 description', stock=1200,
                                        supplier=self.supplier1)
        self.item2 = Item.objects.create(name='Item 2', description='Item 2 description', stock=100,
                                         supplier=self.supplier2)

    def test_count_items(self):
        self.assertEqual(Item.objects.count(), 2)

    def test_correct_pluralization_of_item(self):
        self.assertEqual(Item._meta.verbose_name_plural, 'items')

    def test_correct_pluralization_of_supplier(self):
        self.assertEqual(Supplier._meta.verbose_name_plural, 'suppliers')

    def test_item_listing(self):
        item = Item.objects.filter(name='Item 1').first()
        self.assertEqual(item.supplier.name, "Supplier1")
        self.assertEqual(item.name, "Item 1")
        self.assertEqual(item.description, "Item 1 description")
        self.assertEqual(item.stock, 1200)

    def test_right_foreign_key(self):
        items = Item.objects.all()
        self.assertNotEqual(str(items[0].supplier.id), str(items[len(items)-1].supplier.id))
