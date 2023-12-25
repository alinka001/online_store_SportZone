# Generated by Django 4.2.7 on 2023-12-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
            },
        ),
        migrations.CreateModel(
            name='FavoritesItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='favs.favorites', verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Товар в избранном',
                'verbose_name_plural': 'Товары в избранном',
            },
        ),
    ]
