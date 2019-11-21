from django.test import TestCase, Client
from django.urls import reverse
from aliments_off.models import Products, SaveProducts
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.login(username='Admin', password='123test123')
        self.homepage_url = reverse('homepage')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
    
    def test_homepage_view(self):
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/home.html')
    
    def test_login_view(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')
    
    ''' query and not found '''