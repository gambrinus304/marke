
# импортируем из джанго методы добавления в админку
from django.contrib import admin
# импортируем наши модели
from .models import Product
from .models import Category
from .models import Order

# говорим админке зарегистрировать наши модели
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
