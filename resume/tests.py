from django.test import TestCase
from django.urls import resolve

from .views import index_page

class IndexViewTest(TestCase):
    
    def test_app_root_resolves_index_page(self):
        index = resolve('/resume/')
        self.assertEqual(index.func, index_page)
