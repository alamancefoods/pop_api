from django.test import TestCase
from model_mommy import mommy
from api.models import Item
# Create your tests here.

class ItemTest(TestCase):

    def test_item(self):
        item = mommy.make(Item)
        self.assertTrue(isinstance(item, Item))
