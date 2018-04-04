from django.shortcuts import render
# импортируем из стандартной сборки Django

from django.http import HttpResponse
# Стандартный вью — это обычная питон-функция

from django.views import generic
# импортируем модель для CBV

from .models import Product
# импортируем нашу модель


def index(request):
    browser_info = request.META['HTTP_USER_AGENT']
    return HttpResponse("Привет! Я знаю много информации о твоем браузере {}".format(browser_info))


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    # добавляем объекты модели в контекст под этим именем
    context_object_name = 'products'
    model = Product

# метод для добавления дополнительной информации в контекст


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # передаем в словарь контекста список всех категорий
    context['categories'] = Category.objects.all()
    return context


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
