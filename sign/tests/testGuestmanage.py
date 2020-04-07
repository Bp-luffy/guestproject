# coding=utf-8
from sign.models.createTables import Guest,Event
from django.test import TestCase
from django.contrib.auth.models import User


class GuestManageTest(TestCase):
    '''嘉宾管理'''

    def setUp(self):
        User.objects.create_user('admin03','admin03@mail.com','admin123456')
        Event.objects.create()
