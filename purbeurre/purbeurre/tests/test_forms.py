from django.test import TestCase
from users.forms import UserRegisterForm


class TestForms(TestCase):

    def test_register_form_valid_data(self):
        form = UserRegisterForm(data={
            'username': 'testons',
            'email': 'unmail@quiva.bien',
            'password1': '123test123',
            'password2': '123test123'
        })

        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
