from django.shortcuts import render, redirect

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['этот сайт', 'создан с целью', 'продемонстрировать умения', 'пользования фреймворком Django'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
