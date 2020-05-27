from django.urls import path
from django.conf.urls import url
from .views import ShopCategories, ShopConfig, ShopSubCategories
from . import views

urlpatterns = [
    url('subcategories/(?P<pk>\d+)$', ShopSubCategories.as_view()),
    url('categories/(?P<pk>\d+)$', ShopCategories.as_view()),
    url('(?P<pk>\d+)$', ShopConfig.as_view()),
    path('', views.index, name='index'),
]
