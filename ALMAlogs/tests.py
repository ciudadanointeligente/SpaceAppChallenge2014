# coding=utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client

# Create your tests here.

class IndexTextCase(TestCase):
    def setUp(self):
        pass
    def test_get_home(self):
        '''gets home page'''
        url = reverse("home")
        self.assertTrue(url)
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code, 200)