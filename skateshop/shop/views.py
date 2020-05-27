from django.http import HttpResponse
from rest_framework import serializers, generics
from shop.models import Shop, Category, Sub_Category
from django.http import JsonResponse
from django.core import serializers as coreSerializers
from django.db.models import Q

# Create your views here.
def index(request):
    return HttpResponse("test")


# Serializers define the API representation.
class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ['ID', 'name']


class ShopCategories(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk, format=None):
        return JsonResponse(list(Category.objects.all().filter(FK_Shop = pk).values()), safe=False)


# Serializers define the API representation.
class ShopConfigSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ['ID', 'name', 'logo']


class ShopConfig(generics.RetrieveAPIView):
    serializer_class = ShopConfigSerializer
    queryset = Shop.objects.all()
    def get(self, request, pk, format=None):
        print(pk)
        print(self.queryset.all().filter(ID=pk).values()[0])
        return JsonResponse(self.queryset.all().filter(ID=pk).values()[0], safe=False)
# Serializers define the API representation.
class SubCategoriesSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ['ID', 'name']


class ShopSubCategories(generics.RetrieveAPIView):
    queryset = Sub_Category.objects.all()
    serializer_class = SubCategoriesSerializer

    def get(self, request, pk, format=None):
        categories = Category.objects.all().filter(FK_Shop=pk).values()
        q_objects = Q()
        for category in categories:
            print('xxxxxxxxxxxxxxxxxxxxxxxx')
            print(category['ID'])
            q_objects |= Q(FK_Category = category['ID'])
        print(Sub_Category.objects.all().filter().values())
        return JsonResponse(list(Sub_Category.objects.all().filter(q_objects).values()), safe=False)
