from django.shortcuts import render
# импортируем из стандартной сборки Django

from django.views import generic
# импортируем модель для CBV

from .models import Product, Category, Order
# импортируем нашу модель
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


# stage_3
class ProductCreate(generic.CreateView):
    # название нашего шаблона с формой
    template_name = 'product_new.html'
    # какие поля будут в форме
    fields = '__all__'
    model = Product


class OrderFormView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = '/'
    # выведем только поля, которые нужно заполнить самому человеку
    fields = ['customer_name', 'customer_phone']

    def form_valid(self, form):
        # получаем ID из ссылки и передаем в ORM для фильтрации
        product = Product.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        # передаем в поле товара нашей формы отфильтрованный товар
        form.instance.product = product
        form.instance.user = user
        # super — перезагружает форму, нужен для работы
        return super().form_valid(form)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# наш секретный Вью


class SecretAdminView(UserPassesTestMixin, generic.TemplateView):
    # секретное содержимое
    template_name = 'memes.html'

    # проверяем условие, если пользователь — админ, то вернет True и пустит пользователя
    def test_func(self):
        return self.request.user.is_superuser
