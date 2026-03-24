# auth_utils.py
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from typing import Optional

# Секретный ключ для JWT
SECRET_KEY = "mysecretkey"  # На проде ставь длинный и сложный ключ!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Время жизни токена

# Контекст для хеширования паролей через bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Хеширование пароля
def hash_password(password: str) -> str:
    # bcrypt поддерживает только до 72 байт
    return pwd_context.hash(password[:72])

# Проверка пароля
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password[:72], hashed_password)

# Создание JWT токена
def create_access_token(data: dict, expires_delta: Optional[int] = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt