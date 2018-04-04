
# импортируем из джанго методы добавления в админку
from django.contrib import admin
# импортируем наши модели
from .models import Product
from .models import Category

# говорим админке зарегистрировать наши модели
admin.site.register(Product)
admin.site.register(Category)


def __str__(self):
    return self.title
