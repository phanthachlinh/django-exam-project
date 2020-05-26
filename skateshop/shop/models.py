from django.db import models


# Create your models here.
class Shop(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='uploads/', null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    FK_Shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    FK_Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Size(models.Model):
    ID = models.AutoField(primary_key=True)
    size_value = models.CharField(max_length=100)
    FK_Sub_Category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.size_value


class Brand(models.Model):
    ID = models.AutoField(primary_key=True)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    FK_Size = models.ForeignKey(Size, on_delete=models.CASCADE)
    FK_Sub_Category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    FK_Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
