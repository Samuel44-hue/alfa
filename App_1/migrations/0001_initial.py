# Generated by Django 5.1.2 on 2024-10-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Image', models.ImageField(null=True, upload_to='')),
                ('Product_Name', models.CharField(max_length=250, null=True)),
                ('Product_Cat', models.CharField(max_length=250, null=True)),
                ('Product_Description', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]