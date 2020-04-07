# coding=utf-8
from django.test import TestCase
from sign.models.createTables import Event, Guest


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(event_id=10, name='oneplus 3 event', status=True, limit=2000,
                             address='shenzhen', start_time='2020-04-10 14:00:00')
        Guest.objects.create(event_id=10, realname='alen', phone='13100001111', email='alen@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, 'shenzhen')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13100001111')
        self.assertEqual(result.realname, 'alen')
        self.assertFalse(result.sign)

    def tearDown(self):
        pass
