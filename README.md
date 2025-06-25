# Веб-сайт медицинской диагностики

## Описание:

Сайт для компании медицинской диагностики, содержащий страницы:
1. Главная
2. О компании
3. Наши услуги
4. Контакты
5. Личный кабинет

## Настройка сервера:

1. Подключитесь к своему серверу:
```
ssh user_name@your_server_ip
```
2. Запустите обновления:
```
sudo apt update
sudo apt upgrade
```
3. Настройте брандмауэр и откройте необходимые порты:
```
sudo ufw status
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
```

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:DadashovaYuliya/Web_medical_diagnostics.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Настройте файл .env:
```
cd course_drf_spa/
nano .env

Для работы с django укажите Ваш секретный ключ и статус debug
SECRET_KEY=
DEBUG=

Для проекта используется база данных PostgreSQL. Укажите ваши параметры, предварительно создав пустую БД
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=

Для интеграции с почтой укажите:
EMAIL_USE_SSL=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```
4. Запустите контейнер:
```
docker-compose up
```
5. Автоматизация с CI/CD через GitHub Actions
```
Для автоматизации сборки, тестирования и деплоя проекта используется GitHub Actions.
Создайте новый репозиторий и добавьте все необходимые переменные среды в secrets.
Основные возможности:
1. Автоматическая проверка кода при каждом пуше или pull request.
2. Запуск тестов для обеспечения качества.
3. Автоматический деплой на сервер после успешных проверок.
```

## Приложения

1. Приложение medic, в котором описаны модели Service, Appointment, DiagnosticResult. 


## Контроллеры

1. Для модели Service, Appointment созданы контроллеры на основе generic.


## Маршрутизация:

1. Для представлений Service, Appointment настроена соответствующая маршрутизация.