# coding=utf-8
from sign.models.createTables import Guest, Event
from django.test import TestCase
from django.contrib.auth.models import User


class GuestManageTest(TestCase):
    '''嘉宾管理'''

    def setUp(self):
        User.objects.create_user('admin03', 'admin03@mail.com', 'admin123456')
        Event.objects.create(event_id=20, name='xiaomi5', limit=2000, address='beijing', status=1,
                             start_time='2020-05-01 15:00:00')
        Guest.objects.create(realname='alen', phone=13100002222, email='alen@mail.com', sign=0, event_id=20)
        self.login_user = {'username': 'admin03', 'password': 'admin123456'}

    def test_event_manage_success(self):
        '''测试嘉宾信息：alen'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alen', response.content)
        self.assertIn(b'13100002222', response.content)

    def test_guest_manage_sreach_success(self):
        '''测试嘉宾搜索'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/search_phone/', {'phone': '13100002222'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alen', response.content)
        self.assertIn(b'13100002222', response.content)
