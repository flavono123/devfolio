from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import index_page

class IndexViewTest(TestCase):
    
    def test_app_root_resolves_index_page(self):
        index = resolve('/resume/')
        self.assertEqual(index.func, index_page)

    def test_app_root_render_correct_html(self):
        request = HttpRequest()
        response = index_page(request)
        expected_html = render_to_string('resume/index.html')

        self.assertEqual(expected_html, response.content.decode())
