# Generated by Django 4.1.5 on 2023-01-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='images')),
                ('image2', models.ImageField(upload_to='images')),
                ('image3', models.ImageField(upload_to='images')),
                ('image4', models.ImageField(upload_to='images')),
            ],
        ),
    ]
