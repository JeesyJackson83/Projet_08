from django.test import SimpleTestCase
from django.urls import reverse, resolve
from homepage.views import home, mentions

class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, home)

    def test_mentions_url_resolves(self):
        url = reverse('mentions')
        self.assertEquals(resolve(url).func, mentions)