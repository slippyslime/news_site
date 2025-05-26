# news_site
Сайт для размещения статей с возможностью редактировать и удалить статьи, имеющий главную и информатифную страницы

### Как установить?
1) Клонируйте и перейдите в репозиторий
```
git clone https://github.com/slippyslime/news_site.git
cd news_site
```
2) Создайте и запустите виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
3) Установите зависимости
```
pip install -r requirements.txt
```
4) Перейдите в репозиторий core и выполните миграции
```
cd core
python manage.py migrate
```
5) Запустите сервер и следуйте инструкциям в консоли
```
python manage.py runserver
```
### Опционально
6) Если нужно зайти в админку создайте нового пользователя с правами
```
python manage.py createsuperuser
```

Пет-проект пользователя slippyslime размещенный для заполнения портфолио
