# coding=utf-8
from django.contrib.auth.models import User
from django.test import TestCase
from sign.models.createTables import Event, Guest


class SignIndexActionTest(TestCase):
    '''发布会签到'''

    def setUp(self):
        User.objects.create_user('admin03', 'admin03@mail.com', 'admin123456')
        Event.objects.create(event_id=21, name='xiaomi5', limit=2000, address='beijing', status=1,
                             start_time='2020-05-01 15:00:00')
        Event.objects.create(event_id=22, name='oneplus4', limit=2000, address='shenzhen', status=1,
                             start_time='2020-05-01 15:00:00')
        Guest.objects.create(realname='alen', phone=13100002222, email='alen@mail.com', sign=0, event_id=21)
        Guest.objects.create(realname='alen', phone=13100003333, email='alen@mail.com', sign=1, event_id=22)
        self.login_user = {'username': 'admin03', 'password': 'admin123456'}

    def test_sign_index_action_phone_null(self):
        '''手机号为空'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/sign_index_action/21/', {'phone': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error', response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        '''手机号或发布会id错误'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/sign_index_action/21/', {'phone': '131000000001'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'event id or phone error', response.content)

    def test_sign_index_action_user_sign_has(self):
        '''用户已签到'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/sign_index_action/22/', {'phone': '13100003333'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in', response.content)

    def test_sign_index_action_sign_success(self):
        '''签到成功'''
        response = self.client.post('/sign/login_action/', data=self.login_user)
        response = self.client.post('/sign/sign_index_action/21/', {'phone': '13100002222'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in success！', response.content)
