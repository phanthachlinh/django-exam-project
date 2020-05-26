# Generated by Django 3.0.6 on 2020-05-23 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('FK_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('size_value', models.CharField(max_length=100)),
                ('FK_Sub_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Sub_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('FK_Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Brand')),
                ('FK_Size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Size')),
                ('FK_Sub_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Sub_Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='FK_Sub_Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop'),
        ),
    ]
