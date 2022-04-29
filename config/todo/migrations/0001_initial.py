# Generated by Django 3.2.8 on 2022-04-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='やること')),
                ('description', models.TextField(blank=True, verbose_name='詳細')),
                ('deadline', models.DateField(verbose_name='締め切り')),
            ],
        ),
    ]