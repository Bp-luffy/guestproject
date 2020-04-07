# coding=utf-8
from sign.models.createTables import Event
from django.test import TestCase
from django.contrib.auth.models import User


class EventManageTest(TestCase):
    '''发布会管理'''

    def setUp(self):
        User.objects.create_user('admin02', 'admin02@mail.com', 'admin123456')
        Event.objects.create(name='xiaomi5', limit=2000, address='beijing', status=1, start_time='2020-05-01 14:00:00')
        self.login_user = {'username': 'admin02', 'password': 'admin123456'}

    def test_event_manage_success(self):
        '''测试发布会：xiaomi5'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_event_manage_search_success(self):
        '''测试发布会搜索'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/search_name', {'name', 'xiaomi5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)
