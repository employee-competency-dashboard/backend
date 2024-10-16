# Хакатон Яндекс.Практикум + Росбанк: Разработка дашборда аналитики компетенций групп и сотрудников Росбанка.
![workflow](https://github.com/AIGarifullin/foodgram/actions/workflows/main.yml/badge.svg)

Даты проведения хакатона: 4 сентября - 16 октября 2024 года.

Организаторы: АНО ДПО «Образовательные технологии Яндекса» и ПАО РОСБАНК

[Подробная информация о хакатоне](https://norikov.notion.site/ec7ad9d3121d49d19354777c02454541)

![Header](https://github.com/employee-competency-dashboard/rosbank_backend/blob/main/frontend/public/Title.png?raw=true)

## Сведение о команде
- [Никита Мальцев](https://t.me/nikfromrus), PM команды,
- [Борис Руденко](https://t.me/barudenko), аналитик данных,
- [Дмитрий Стреленко](https://t.me/d_strelen), системный аналитик,
- [Басанг Амулаков](https://t.me/basang13), бизнес-аналитик,
- [Анна Юдина](https://t.me/yudina_a), дизайнер,
- [Мария](https://t.me/madam_entu), дизайнер,
- [Максим Романенко](https://t.me/MaxRMNK), frontend-разработчик,
- [Адель Гарифуллин](https://github.com/AIGarifullin), python-разработчик,
- [Сергей Виноградов](https://github.com/yan-gabala), python-разработчик.


## Ссылка на Swagger
[Ссылка на файл Хакатон Росбанк API.yaml](https://drive.google.com/file/d/1lmD_IYijZIhM2rTudHt33aJe0Xexm9Oj/view?usp=drive_link)

## Примеры запросов:
> Подробнее можно ознакомится в документации Redoc https://rosbankdashboard.ddns.net/dashboards/teams/schema/redoc/

> Подробнее можно ознакомится в документации Swagger https://rosbankdashboard.ddns.net/dashboards/teams/schema/swagger/

## Инструкция по сборке и запуску
### Запуск локальной версии проекта
Перейти в директорию с файлом **docker-compose.yml**, выполнить запуск и миграции:

```
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/static/. /backend_static/static/
```

### Отличия обычной версии проекта от продакш
Продакш-версия проекта позволяет:
* Автоматизировать запуск и обновление приложения;
* Сделать запуск приложения воспроизводимым на любых серверах, независимо от настроек.

### Запуск продакш-версии проекта
Для этого необходимо:
1. Собрать образы `rosbank_frontend`, `rosbank_backend` и `rosbank_gateway` и залить их на Docker Hub:

    ```
    cd frontend
    docker build -t username/rosbank_frontend .
    cd ../backend
    docker build -t username/rosbank_backend .
    cd ../infra
    docker build -t username/rosbank_gateway .
    ```
    ```
    docker push username/rosbank_frontend
    docker push username/rosbank_backend
    docker push username/rosbank_gateway
    ```    
2. Создать в корневой директории проекта файл конфигурации **docker-compose.production.yml**, который будет использовать собранные образы на Docker Hub и управлять запуском контейнеров на продакш-сервере. Отличие нового файла конфигурации от **docker-compose.yml** состоит в замене `build` на `image` с указанием ссылки на образ (`postgres:13.10` для `db`, `username/rosbank_frontend` для `frontend`, `username/rosbank_backend` для `backend` и `username/rosbank_gateway` для `gateway`).  

3. Развернуть и запустить Docker на сервере. Поочередно выполнить на сервере следующие команды:
    ```
    sudo apt update
    sudo apt install curl
    curl -fSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh
    sudo apt install docker-compose-plugin
    ```
4. Загрузить на сервер новый файл конфигурации для Docker Compose и запустить контейнеры.
    Поместить в директорию проекта на сервере файл конфигурации **docker-compose.production.yml**, а также файл **.env**.
    Выполнить команду на сервере в папке проекта:
    ```
    sudo docker compose -f docker-compose.production.yml up -d
    ```
    Выполнить миграции, собрать статические файлы бэкенда и скопировать их в `/backend_static/static/`:
    ```
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
    sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/static/. /backend_static/static/
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
    ```
5. Настроить «внешний» Nginx, что вне контейнера — для работы с приложением в контейнерах.
    Открыть файл **default** конфигурации Nginx:
    
    ```
    sudo nano /etc/nginx/sites-enabled/default
    ```
    Изменить настройки `location` в секции `server` (три блока `location` заменить на один):
    ```
    location / {
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:7000;
    }
    ```
    Сделать проверку и перезагрузку файла конфигурации:
    ```
    sudo nginx -t
    sudo service nginx reload
    ```

6. Подготовить свой удаленный сервер к публикации проекта. Очистить диск сервера от лишних данных (кеш npm, APT, старые системные логи):
    ```
    npm cache clean --force
    sudo apt clean
    sudo journalctl --vacuum-time=1d
    ```
    Полезно будет выполнить команду `sudo docker system prune -af`: она уберёт все лишние объекты, которые вы могли создать в докере за время выполнения заданий спринта, — неиспользуемые контейнеры, образы и сети.

7. Для автоматизации запуска и обновления проекта на продакш-сервере создать в директории `.github/workflows` файл **main.yml** с описанием *workflow*. Сделать коммит проекта и разместить его в удаленный репозиторий:
    ```
    git add .
    git commit -m 'Add Actions'
    git push
    ```
    Для управления процессами *CI/CD* (*Continuous Integration/Continuous Delivery*) открыть раздел *Actions* в репозитории проекта в своем аккаунте.

## Стек проекта
Python, Django REST Framework, Nginx, DNS, HTTPS, Docker, PostgreSQL, GitHub Actions

