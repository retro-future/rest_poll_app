# User Survey Applications API

Задача: спроектировать и разработать API для системы опросов пользователей.

### _Документация API_ доступно по адресу http://127.0.0.1:8000/swagger/ (автодокументирование с помощью swagger (drf-yasg))

## Описание ТЗ:

##### _Функционал для администратора системы:_
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##### _Функционал для пользователей системы:_
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя


## Языки и фреймворки:
  * Python 3.9
  * Django 3.2.9
  * Djangorestframework 3.12.4



Склонируйте репозиторий с помощью git:

    https://github.com/retro-future/rest_poll_app.git

Перейти в папку:
```bash
cd poll_app_rest
```

Создать и активировать виртуальное окружение(venv) Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Нужно создать суперпользователя
```bash
python manage.py createsuperuser
```
* Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/

___

### Чтобы получить токен пользователя: 
>* Request method: POST
>* URL: http://localhost:8000/api-auth/token/login/
>* Body: 
>    * username: 
>    * password: 
#### Example:
```
curl --location --request POST 'http://localhost:8000/api-auth/token/login/' \
--form 'username=%username' \
--form 'password=%password'
```

#### Результат будет таким:
> { "auth_token": "bdd246f0797448214256d2b0d34fe541121cccc7" }

___

### Чтобы создать опрос:
* Request method: POST
* URL: http://localhost:8000/api/surveysApp/create/
* Header:
   *  Authorization: Token userToken
* Body:
    * name: name of poll
    * description: description of poll
    * start_time: publication date can be set only when survey is created, format: YYYY-MM-DD HH:MM:SS
    * end_time: poll end date, format: YYYY-MM-DD HH:MM:SS
    
* Example: 
```
curl --location --request POST 'http://localhost:8000/api/polls/create/' \
--header 'Authorization: Token %userToken' \
--form 'name=%poll_name' \
--form 'description=%poll_description' \
--form 'start_time=%start_time' \
--form 'end_time=%end_time 
```

___

### Обновить опрос:
* Request method: PATCH
* URL: http://localhost:8000/api/polls/update/<poll_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id 
* Body:
    * name: name of survey
    * description: description of poll
    * end_time: poll end time, format: YYYY-MM-DD HH:MM:SS
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/polls/update/<poll_id>/' \
--header 'Authorization: Token %userToken' \
--form 'name=%poll_name' \
--form 'description=%poll_description' \
--form 'end_time=%end_time 
```

___


### Удалить опрос:
* Request method: DELETE
* URL: http://localhost:8000/api/polls/delete/<poll_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * poll_id
Example:
```
curl --location --request DELETE 'http://localhost:8000/api/polls/delete/<poll_id>/' \
--header 'Authorization: Token %userToken'
```

___


### Посмотреть все опросы:
* Request method: GET
* URL: http://localhost:8000/api/polls/view/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/polls/view/' \
--header 'Authorization: Token %userToken'
```

___

### Просмотр текущих активных опросов:
* Request method: GET
* URL: http://localhost:8000/api/polls/view/active/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/polls/view/active/' \
--header 'Authorization: Token %userToken'
```

___

### Создаем вопрос:
* Request method: POST
* URL: http://localhost:8000/api/question/create/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll 
    * text: 
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'text=%question_text' \
--form 'question_type=%question_type \
```

___

### Обновляем вопрос:
* Request method: PATCH
* URL: http://localhost:8000/api/question/update/<question_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * poll: id of poll 
    * text: question_text
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/<question_id>/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'text=%question_text' \
--form 'question_type=%question_type \
```

___

### Удаляем вопрос:
* Request method: DELETE
* URL: http://localhost:8000/api/question/update/<question_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/question/delete/<question_id>' \
--header 'Authorization: Token %userToken' 
```
___
### Создаем Ответ:
* Request method: POST
* URL: http://localhost:8000/api/answer/create/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * text: answer_text
* Example:
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%id_of_question' \
--form 'text=%answer_text'
```
___
### Обновляем Ответ:
* Request method: PATCH
* URL: http://localhost:8000/api/answer/update/<answer_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * question: id of question
    * text: answer_text
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/<answer_id>/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'text=%answer_text'
```
___

### Удаляем ответ:
* Request method: DELETE
* URL: http://localhost:8000/api/answer/delete/<answer_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/delete/<answer_id>/' \
--header 'Authorization: Token %userToken' 
```

___

### Создаем выбор пользователя:
* Request method: POST
* URL: http://localhost:8000/api/user_answers/create/
* Header:
    * Authorization: Token userToken
* Body:
    * poll: id of poll
    * question: id of question
    * answer: if question type is one or multiple then it’s id of answer else null
    * answer_text: if question type is text then it’s text based answer else null

>### <span style="color:red">_Нужно передать либо answer_id либо answer_text_</span>
* Example:
```
curl --location --request POST 'http://localhost:8000/api/user_answers/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll_id' \
--form 'question=%question_id' \
--form 'answer=%answer_id \
--form 'answer_text=%answer_text'
```

___

### Обновляем выбор пользователя:
* Request method: PATCH
* URL: http://localhost:8000/api/user_answers/update/<answer_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * poll: id of poll
    * question: id of question
    * answer: if question type is one or multiple then it’s id of answer else null
    * answer_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/user_answers/update/<answer_id>' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll_id' \
--form 'question=%question_id' \
--form 'answer=%answer_id \
--form 'answer_text=%answer_text'
```

___

### Удаляем выбор пользователя:
* Request method: DELETE
* URL: http://localhost:8000/api/user_answers/delete/<answer_id>/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

___

### Просматриваем ответы пользователя:
* Request method: GET
* URL: http://localhost:8000/api/user_answers/view/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/user_answers/view/' \
--header 'Authorization: Token %userToken'
```

___