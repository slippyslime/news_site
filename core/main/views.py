from django.shortcuts import render, redirect

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['а вот тут', 'я демонстрирую во вьюхах', 'умение отправлять данные', 'в темплейты']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')