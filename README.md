# Simple Project
---


Django проект для работы с базой Заказчиков и Поставщиков.


### Шаблоны
`core/base.html` - базовый шаблон

`core/index.html` - шаблон главной страницы

`core/provider.html` - шаблон страницы поставщика

`core/providers.html` - шаблон страницы поиска поставщиков


### URLs
Главная страница: `/`

Страница поиска: `/search/?name_customer=<name_customer>`

Страница поставщика: `/provider/<provider_id>/`


### Запуск проекта на localhost
Команда запуска сервера:
```python3
python3 ./manage.py runserver
```

После выполнения этой команды откройте `127.0.0.1:8000` в браузере.