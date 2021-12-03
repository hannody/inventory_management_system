from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from inventory.models import Supplier, Item


class ItemsViewTest(TestCase):
    """
    Test the views for the items
    """
    client = APIClient()
    list_api_endpoint = '/api/inventory/'
    detail_endpoint = 'inventory/'
    list_inventory_endpoint = '/inventory/'

    def setUp(self):
        """
        Data preparation to be used in tests i.e. creating objects of Item Model for testing purposes.
        """
        # Preparing data for testing.
        self.supplier1 = Supplier.objects.create(name='Bega Cheese', address='Bega Valley, NSW', category='L')

        self.item = Item.objects.create(name='Slice Cheese', description='84 Slices of cheddar for Burger', stock=560,
                                        supplier=self.supplier1)

        # Creating an authenticated user for testing purposes.
        self.user = User.objects.create_user(
            username='username',
            email='super@user.com',
            password='foo',
            is_staff=True
        )

    def test_list_inventory_api_view(self):
        """
        Test the list inventory api view i.e. '/api/inventory/'
        """
        # Unauthenticated user action.
        response = self.client.get(path=self.list_api_endpoint)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action.
        self.client.login(username='username', email='super@user.com', password='foo')
        response = self.client.get(path=self.list_api_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_inventory_view(self):
        """
        Test the list inventory view i.e. '/inventory/'
        """
        # Unauthenticated user action, expected outcome ==> 403_FORBIDDEN
        response = self.client.get(path=self.list_inventory_endpoint)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action, expected outcome ==> 200_OK
        self.client.login(username='username', email='super@user.com', password='foo')
        response = self.client.get(path=self.list_inventory_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_api_view(self):
        """
        Test the detail api view i.e. 'inventory/<uuid:pk>/'
        """

        url = '/{}{}/'.format(self.detail_endpoint, self.item.id)

        # Unauthenticated user action, expected outcome ==> 403_FORBIDDEN
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated user action, expected outcome ==> 200_OK
        self.client.login(username="username", email='normal@user.com', password='foo')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

