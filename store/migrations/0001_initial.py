# Generated by Django 4.1.1 on 2022-09-27 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='images')),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
