from fastapi import FastAPI

from app.routers.users import router as users_router

app = FastAPI(
    title="Team finder API",
    description= "Платформа для поиска людей в команду"
)

app.include_router(users_router)

@app.get("/")
def root():
    return{"messege":"web lab1 is running"}