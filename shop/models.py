from django.db import models
# Импортируется родительский класс моделей


class Product(models.Model):
    # Создаем базовую модель нашего продукта
    title = models.CharField(max_length=200)
    # и указываем максимальную длину поля
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
