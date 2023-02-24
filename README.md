# hw04_tests
# Описание проекта
Данный проект предназначен для тестирования приложения Yatube.

# Технологии
django-debug-toolbar==2.2
django==2.2.16
pytest-django==3.8.0
pytest-pythonpath==0.7.3
pytest==5.3.5
requests==2.22.0
six==1.14.0
sorl-thumbnail==12.6.3
mixer==7.1.2
Faker==12.0.1



# Запуск проекта
Клонируйте репозиторий на своё устройство:<br>
```git clone <ссылка на проект>```

Перейдите в директорию:<br>
```cd api_final_yatube```

Разверните виртуальное окружение:<br>
```python -m venv env или source env/bin/activate ```

Обновите pip:<br>
```python -m pip install --upgrade pip```

Установите зависимости из файла requirements.txt:<br>
```pip install -r requirements.txt```

Выполнить миграции:<br>
```python3 manage.py migrate```

Запустить проект:<br>
```python manage.py runserver```

# Автор
- Григорян Арсен
