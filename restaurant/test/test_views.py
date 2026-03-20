from django.test import TestCase
from decimal import Decimal
from ..models import MenuItem
from ..serializers import MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(
            username='tester',
            password='12345'
        )
        
        self.client.force_login(user=self.user)
        
        MenuItem.objects.create(title = 'Frijoles Borrachos', price=Decimal("10.00"), inventory=5)
        MenuItem.objects.create(title = 'Bandeja Paisa', price=Decimal("8.50"), inventory=7)
        
        self.url = "/restaurant/menu-items/"
        
    def test_getall(self):
        response = self.client.get(self.url)
        
        items = MenuItem.objects.all().order_by('id')
        expected = MenuItemSerializer(items, many=True).data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)
        