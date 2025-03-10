# Документация по API проекта Focusy

## Описание
На данный момент в директориях находится в папке src все визуальные компоненты на vue.js. В python файлах находится Backend написанный на FastApi.
## Установка

### Требования
- Python 3.10+
- Установленный пакетный менеджер `pip`

### Установка зависимостей
```sh
pip install -r requirements.txt
```

### Запуск проекта
```sh
uvicorn main:app --reload
```

## Структура файлов
- `main.py` — основной файл с API-эндпоинтами
- `models.py` — модели базы данных
- `requests.py` — функции для API-эндпоинтов
- `bot.py` — код телеграмм бота на aiogram

## API-эндпоинты

### 1. Получение количества выполненных заданий
#### Запрос
```http
GET /api/all_completed/{tg_id}
```
#### Описание
Возвращает количество всех выполненных заданий пользователем.

### 2. Получение количества выполненных заданий по теме
#### Запрос
```http
GET /api/theme_completed/{tg_id}/{theme}
```
#### Описание
Возвращает количество выполненных заданий пользователем в определенной категории.

### 3. Получение статистики пользователя
#### Запрос
```http
GET /api/stats/{tg_id}
```
#### Описание
Возвращает информацию о пользователе: количество XP и монет.

### 4. Изменение количества монет
#### Запрос
```http
POST /api/change_coins/{tg_id}/{amount}
```
#### Описание
Изменяет баланс монет у пользователя.

### 5. Изменение количества XP
#### Запрос
```http
POST /api/change_xp/{tg_id}/{amount}
```
#### Описание
Изменяет количество опыта (XP) у пользователя.

### 6. Получение невыполненных заданий
#### Запрос
```http
GET /api/incomplete-tasks/{tg_id}/{theme}
```
#### Описание
Возвращает список невыполненных заданий для пользователя в заданной категории.

### 7. Получение доступных тем заданий
#### Запрос
```http
GET /api/theme-tasks/{tg_id}
```
#### Описание
Возвращает список доступных тем заданий для пользователя.

### 8. Отметка задания как выполненного
#### Запрос
```http
POST /api/mark_complete/{tg_id}/{task_id}
```
#### Описание
Помечает конкретное задание как выполненное для пользователя.

### 9. Сброс выполненных заданий по теме
#### Запрос
```http
POST /api/full_to_incomplete/{tg_id}/{theme}
```
#### Описание
Помечает все задания по определенной теме как невыполненные.

## Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной по email: `your_email@example.com`.

