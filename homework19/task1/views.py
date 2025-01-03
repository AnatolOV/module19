from django.shortcuts import render, redirect

from django.shortcuts import render
from task1.forms import UserRegister

from .models import Buyer, Game


# Create your views here.
def platform_view(request):
    return render(request, 'fouth_task/menu.html')


def shop_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fouth_task/shop.html', context)


def cart_view(request):
    return render(request, 'fouth_task/cart.html')


def process_registration(request):
    # Пустой словарь для информации
    info = {}

    form = UserRegister(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            if Buyer.objects.filter(name=username).exists():
                info['error'] = "Пользователь с таким именем уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            else:
                # Создание нового пользователя в таблице Buyer
                Buyer.objects.create(name=username, balance=777, age=age)
                info['success'] = "Вы успешно зарегистрированы!"
                # return redirect('login')
                return render(request, 'fifth_task/registration_page.html', {'form': UserRegister(), 'info': info})
    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})


def sign_up_by_django(request):
    return process_registration(request)


def sign_up_by_html(request):
    return process_registration(request)
