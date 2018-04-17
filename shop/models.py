from django.db import models
# Импортируется родительский класс моделей
from django.urls import reverse


class Product(models.Model):
    # Создаем базовую модель нашего продукта
    title = models.CharField(max_length=200)
    # и указываем максимальную длину поля
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey(
        'Category', related_name="products", on_delete='models.CASCADE', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

# вот тут вообще не уверен, но добавил по аналогии и вроде заработало
    def get_absolute_url(self):
        return reverse('product_order', args=[str(self.id)])


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete='CASCADE')
