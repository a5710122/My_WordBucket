from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from wordbucket.views import home_page  
from wordbucket.models import Item

class HomePageTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'admin',
            'password': 'wordbucket'}
        User.objects.create_user(**self.credentials)	

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
         
    def test_login(self):
            # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
            # should be logged in now
        response.context['user'].is_authenticated
        

