from django.test import TestCase
from django.urls import resolve
from blog.views import post_list
from django.http import HttpRequest
#from selenium import webdriver

class HomePageTest(TestCase):

    def test_root_url_resolves_to_post_list(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)


    def test_base_html_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith("{% extends 'blog/base.html' %}"))
        self.assertIn('<p>published: {{ post.published_date }}</p>', html)
        self.assertTrue(html.endswith('{% endblock %}'))
