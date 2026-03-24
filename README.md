# Система аутентификации и RBAC

## Роли
- admin
- user

## Ресурсы
- users

## Действия
- read
- update
- delete

## Таблица прав (Role-Permission)
| Роль  | Ресурс | Действия         |
|-------|--------|-----------------|
| admin | users  | read, delete, update |
| user  | users  | read             |

## Поведение
- Soft delete: is_active=False
- JWT токен хранит user_id
- 401: нет токена
- 403: недостаточно прав