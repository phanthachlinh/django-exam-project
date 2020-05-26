from django.http import HttpResponse
from rest_framework import serializers, generics
from shop.models import Shop, Category, Sub_Category
from django.http import JsonResponse


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
        print(pk)
        return JsonResponse(list(Category.objects.all().values()), safe=False)


# Serializers define the API representation.
class ShopConfigSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ['ID', 'name', 'logo']


class ShopConfig(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopConfigSerializer

    def get(self, request, pk, format=None):
        print(pk)
        return JsonResponse(list(Shop.objects.all().filter(ID=pk).values()), safe=False)


# Serializers define the API representation.
class SubCategoriesSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = ['ID', 'name', 'logo']


class ShopSubCategories(generics.RetrieveAPIView):
    queryset = Sub_Category.objects.all()
    serializer_class = SubCategoriesSerializer

    def get(self, request, pk, format=None):
        print(pk)
        print(Sub_Category.objects.all().values())
        return JsonResponse(list(Sub_Category.objects.all().filter(FK_Category_id=pk).values()), safe=False)
