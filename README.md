# RBAC Auth App

Приложение на FastAPI для регистрации и авторизации пользователей с поддержкой RBAC (Role-Based Access Control).

## Возможности

- Регистрация пользователей (`/auth/register`)
- Авторизация и получение JWT токена (`/auth/login`)
- Проверка ролей и прав доступа для различных эндпоинтов
- Хранение паролей с хэшированием
- Простая структура для расширения и интеграции в другие проекты

## Установка и запуск

Клонируем репозиторий, создаем виртуальное окружение, устанавливаем зависимости и запускаем приложение:

```bash
git clone https://github.com/RomanTheDev-cmd/rbac_auth_app.git
cd rbac_auth_app

# Создаем и активируем виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # для macOS/Linux
# venv\Scripts\activate   # для Windows

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем приложение
uvicorn main:app --reload