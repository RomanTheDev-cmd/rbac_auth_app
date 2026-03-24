from fastapi import FastAPI
from routers import auth_router
from database import Base, engine

# создаем таблицы в базе
Base.metadata.create_all(bind=engine)

app = FastAPI(title="RBAC Auth App")

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])