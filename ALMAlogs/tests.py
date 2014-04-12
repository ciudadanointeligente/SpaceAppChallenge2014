# coding=utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

class IndexTextCase(TestCase):
    def setUp(self):
        pass
    def test_get_home(self):
        '''gets home page'''
        url = reverse("home")
        self.assertTrue(url)