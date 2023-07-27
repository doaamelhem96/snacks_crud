from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse
# Create your tests here.
class Snacktest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random',email='random@random.com',
            password='random@12345'
        )
        self.snack = Snack.objects.create(
           title = 'test',
           purchaser = self.user,
           description="anythings"
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')

    def test_detail_view(self):
        url = reverse('details',args=[self.snack.id])  
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_detail.html')


    def test_create_view(self):
        url = reverse('snack_create')
        data={
            "title": "test_2",
            "purchaser" : self.user.id,
            "description": "anythings"
        }


        response = self.client.post(path=url,data = data,follow = True)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response, reverse('details',args=[2]))


    def test_update_view(self):
        url = reverse('sna_updates',args=[self.snack.id])
        data = {
            'title' :'test_2',
            'purchaser' : self.user.id,
            'description' : 'anythings'
        }
        res = self.client.post(path=url,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),1)
        self.assertTemplateUsed(res,'snack_list.html')
        self.assertRedirects(res,reverse('snacklist'))

    def test_delete_view(self):
        url = reverse('sna_delete',args=[self.snack.id])
        res = self.client.post(path=url,follow=True)
        self.assertEqual(len(Snack.objects.all()),0)
        self.assertTemplateUsed(res,'snack_list.html')
        self.assertRedirects(res,reverse('snacklist'))

    def test_fields_model(self):
        self.assertEqual(self.snack.purchaser,self.user)
        self.assertEqual(self.snack.title,'test')
        self.assertEqual(self.snack.description,'anythings')
class test_Home(TestCase):
    def test_status_code(self):
        url=reverse('home')
        response=self.client.get (url)
        self.assertEqual (response.status_code,200)
        
    def test_Template(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
class SnacksListViewsTest(TestCase):
    def setUp(self):
       
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

       
        self.snack = Snack.objects.create(
            title='Test Snack',
            purchaser=self.user,
            description='A test snack'
        )

    def test_snacks_list_view(self):
        url = reverse('snacklist')
        response = self.client.get(url)

        
        self.assertEqual(response.status_code, 200)

        
        self.assertTemplateUsed(response, 'snack_list.html')

       
        self.assertIn('snack', response.context)

       
        self.assertEqual(response.context['snack'], self.snack)
