# Generated by Django 2.2.16 on 2020-09-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listecourse', '0002_liste'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='illustration',
            field=models.ImageField(default='addProduct/notfound.jpg', upload_to='addProduct/'),
        ),
    ]
