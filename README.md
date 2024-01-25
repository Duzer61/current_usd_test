
# Проект "Current_usd". Написан в качестве тестового задания для [Photo Point](https://www.photo-point.ru/)

### Описание задания:

> Предлагаем вам создать "голый" джанго проект, который по переходу на
> страницу /get-current-usd/ будет отображать в json формате актуальный
> курс доллара к рублю (запрос по апи, найти самостоятельно) и
> показывать 10 последних запросов (паузу между запросами курсов должна
> быть не менее 10 секунд)

Для получения курса доллара использовал api сервиса https://app.freecurrencyapi.com/
### Краткая инструкция по запуску в dev режиме:
- скачать проект на локальную машину `git clone git@github.com:Duzer61/current_usd_test.git`
- перейти в директорию с проектом `/current_usd_test/`
- создать виртуальное окружение командой `python3 -m venv venv` (команда для Linux. Для Windows или macOS может отличаться. В проекте применялся python3.12)
- активировать виртуальное окружение  `source venv/bin/activate` (для Windows `source venv/Scripts/activate`)
- установить зависимости. При активированном виртуальном окружении выполнить команду: `pip install -r requirements.txt`
- перейти в директорию `current_usd`
- переименовать файл `.env_example` в `.env` `mv .env_example .env` и при необходимости внести свои данные (т.к. в данном случае API_KEY не является секретным - я оставил в настройках действующий api_key для возможности проверки задания)
- применить миграции `python3 manage.py migrate`
- запустить проект в dev режиме `python3 manage.py runserver`
- GET запросы можно делать по адресу: `http://localhost:8000/get-current-usd/` с помощью какого-либо приложения для тестирования api (например Postman)
- в файле `/current_usd/constants.py` можно изменить настройки времени кэширования, количества последних результатов для вывода, и валюты для запроса курса по отношению к доллару.

 ## Автор
Данил Кочетов - [GitHub](https://github.com/Duzer61)
