from django.test import SimpleTestCase
from django.urls import reverse, resolve
from homepage.views import home, mentions
from users.views import register, profile
from aliments_off.views import SearchView, ResultView, DetailProductView, SaveView, MyProductsView


class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, home)

    def test_mentions_url_resolves(self):
        url = reverse('mentions')
        self.assertEquals(resolve(url).func, mentions)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    # def test_login_url_resolves(self):
    #     url = reverse('login')
    #     self.assertEquals(resolve(url).func, login)

    # def test_logout_url_resolves(self):
    #     url = reverse('logout')
    #     self.assertEquals(resolve(url).func, logout)

    def test_search_url_resolves(self):
        url = reverse('aliments_off:search')
        self.assertEquals(resolve(url).func.view_class, SearchView)

    def test_result_url_resolves(self):
        url = reverse('aliments_off:result', args=['15'])
        self.assertEquals(resolve(url).func.view_class, ResultView)

    def test_detail_url_resolves(self):
        url = reverse('aliments_off:detail', args=['155'])
        self.assertEquals(resolve(url).func.view_class, DetailProductView)

    def test_save_url_resolves(self):
        url = reverse('aliments_off:save')
        self.assertEquals(resolve(url).func, SaveView)

    def test_myproducts_url_resolves(self):
        url = reverse('aliments_off:myproducts')
        self.assertEquals(resolve(url).func.view_class, MyProductsView)