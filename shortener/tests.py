from django.test import TestCase
from django.urls import reverse
from django.utils.safestring import SafeString
from .views import ShortenURLView
from .models import ShortenedURLModel
from .forms import ShortenURLForm


# Create your tests here.

class FormTest(TestCase):

    form = ShortenURLForm()

    def test_form_safeString(self):
        self.assertTrue(self.form.fields, SafeString)


class shortenerURLViewTest(TestCase):
    view_test = ShortenURLView()

    def setUp(self):
        pass

    def test_check_add_type(self):
        self.assertTrue()

    def test_generate_short_code(self):
        self.assertEqual(len(self.view_test.generate_short_code()), 6)
        self.assertEqual(self.view_test.generate_short_code().isalnum(), True)
