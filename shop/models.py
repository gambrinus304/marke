# Импортируется родительский класс моделей
from django.db import models

# Создаем базовую модель нашего продукта


class Product(models.Model):
    # и указываем максимальную длину поля
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey(
        'Category', related_name="products", on_delete='CASCADE', null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title
