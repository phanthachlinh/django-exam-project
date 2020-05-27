from django.test import TestCase
from .models import Shop,Category,Sub_Category
from django.core import serializers
from rest_framework.test import APITestCase
from .views import ShopConfig,ShopCategories,ShopSubCategories
from rest_framework.test import APIRequestFactory
from rest_framework.renderers import JSONRenderer

import json

# Create your tests here.
class ShopApiTest(TestCase):
    shop1 = ''
    shop2 = ''
    def setUp(self):
        self.shop1 = Shop.objects.create(name="shop1")
        self.shop2 = Shop.objects.create(name="test name 2")
        self.shop1.save()
        self.shop2.save()

    def test_shop_api_call(self):
        factory = APIRequestFactory()
        view = ShopConfig.as_view()

        # Make an authenticated request to the view...
        request = factory.get('/shops/')
        response = json.loads(view(request,pk=2).content)
        self.assertEqual(self.shop2.name,response['name'])


class ShopCategoriesTest(TestCase):
    shop1 = ''
    shopCategory1 = ''
    shopCategory2 = ''
    def setUp(self):
        self.shop1 = Shop.objects.create(name="shop1")
        self.shop1.save()
        self.shopCategory1 = Category.objects.create(name="category 1",FK_Shop_id='1')
        self.shopCategory1.save()
        self.shopCategory2 = Category.objects.create(name="category 2",FK_Shop_id='1')
        self.shopCategory2.save()

    def test_shop_category_api_call(self):
        factory = APIRequestFactory()
        view = ShopCategories.as_view()

        # Make an authenticated request to the view...
        request = factory.get('shops/categories/1')
        response = json.loads(view(request,pk=1).content)
        self.assertEqual(len(response), 2)

class ShopSubCategoriesTest(TestCase):
    shop1 = ''
    shopCategory1 = ''
    shopCategory2 = ''
    def setUp(self):
        self.shop1 = Shop.objects.create(name="shop1")
        self.shop1.save()
        self.shopCategory1 = Category.objects.create(name="category 1",FK_Shop_id='1')
        self.shopCategory1.save()
        self.shopSubCategory1 = Sub_Category.objects.create(name="sub category 2",FK_Category_id='1')
        self.shopSubCategory1.save()
        self.shopSubCategory2 = Sub_Category.objects.create(name="sub category 2",FK_Category_id='1')
        self.shopSubCategory2.save()

    def test_shop_sub_category_api_call(self):
        factory = APIRequestFactory()
        view = ShopSubCategories.as_view()

        # Make an authenticated request to the view...
        request = factory.get('shops/subcategories/1')
        #response = json.loads(view(request,pk=1).content)
        #print(response)
        #self.assertEqual(len(response), 2)
