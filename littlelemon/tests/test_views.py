from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Burger", price=120, inventory=50)
        
def test_getall(self):
        url = reverse("menu-list")  # Assuming you have a URL pattern named "menu-list" for the Menu API view
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)