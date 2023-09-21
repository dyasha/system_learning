# System_Learning
### Онлайн-платформа для обучения
## Описание
### Проект представляет собой онлайн-платформу для обучения, где пользователи могут создавать и продавать образовательные курсы, а также просматривать доступные уроки и отслеживать свой прогресс.

## Технологии
- Django
- DRF
- Python 
- Swagger

## Установка и запуск 
1. Установите Poetry, если он еще не установлен:

   >https://python-poetry.org/docs/#installation

2. Склонируйте репозиторий и перейдите в его директорию:
   >git clone https://github.com/dyasha/system_learning.git

   >cd system_learning
3. Установите зависимости с помощью Poetry:

    >poetry shell

    >poetry install

4. Выполните миграции:
    >python manage.py migrate
5. Запустите программу, выполнив следующую команду:
    >python manage.py runserver

## Модели данных

### Product (Продукт)

- name (CharField): Название продукта.
- owner (ForeignKey): Владелец продукта, связанный с моделью пользователя. 

### Lesson (Урок)
- title (CharField): Название урока.
- video_url (URLField): Ссылка на видеоурок.
- duration_seconds (PositiveIntegerField): Длительность урока в секундах.
- products (ManyToManyField): Связь с продуктами, в которых доступен урок.
### Access (Доступ)
- user (ForeignKey): Пользователь, получивший доступ к продукту.
- product (ForeignKey): Продукт, к которому пользователь имеет доступ.
### LessonView (Просмотр урока)
- user (ForeignKey): Пользователь, просматривающий урок.
- lesson (ForeignKey): Урок, который просматривается.
- start_time (DateTimeField): Время начала просмотра урока (автоматически добавляется).
- end_time (DateTimeField): Время окончания просмотра урока (может быть пустым).
- status (CharField): Статус просмотра урока ("Просмотрено" или "Не просмотрено").

## API
API Доступно по этому адресу:
- 127.0.0.1:8000/swagger/


## __Автор__
###  [Береснев Владислав](https://github.com/dyasha)
>А [здесь](https://gitlab.com/dyasha) расположен мой gitlab =)