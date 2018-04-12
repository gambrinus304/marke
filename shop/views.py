from django.shortcuts import render
# импортируем из стандартной сборки Django

from django.views import generic
# импортируем модель для CBV

from .models import Product
from .models import Category
# импортируем нашу модель


class ProductListView(generic.ListView):
    template_name = 'products_list.html'
    # подключаем наш Темплейт
    context_object_name = 'products'
    # под каким именем передадутся данные в Темплейт
    model = Product
    # название Модели

    def get_context_data(self, **kwargs):
        # метод для добавления дополнительной информации в контекст
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий
        context['categories'] = Category.objects.all()
        return context


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'details'
    model = Product


class CategoryListView(generic.ListView):
    template_name = 'product_category.html'
    context_object_name = 'categories'
    model = Category


class CategoryDetail(generic.DetailView):
    template_name = 'category_detail.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
