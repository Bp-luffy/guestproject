# coding=utf-8
from django.test import TestCase
from django.contrib.auth.models import User


class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin01', 'admin01@email', 'admin123456')

    def test_add_admin(self):
        '''测试添加用户'''
        user = User.objects.get(username='admin01')
        self.assertEqual(user.username, 'admin01')
        self.assertEqual(user.email, 'admin01@mail.com')

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/sign/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/sign/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        '''登录成功'''
        test_data = {'username': 'admin01', 'password': 'admin123456'}
        response = self.client.post('/sign/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)
