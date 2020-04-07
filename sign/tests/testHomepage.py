# coding=utf-8
from django.test import TestCase


class HomePageTest(TestCase):
    '''测试index登录首页'''

    def test_home_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/sign/index')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
