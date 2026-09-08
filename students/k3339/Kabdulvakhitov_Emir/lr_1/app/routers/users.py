from app.models.users import User, Profile, Project


users_db: list[User] = [
    User(
        id=1,
        username="emir",
        email="emir@example.com",
        profile=Profile(
            first_name="Эмир",
            last_name="Кабдулвахитов",
            bio="Frontend developer"
        ),
        projects=[
            Project(
                id=1,
                title="AI Business Agent",
                description="AI-сервис для анализа B2B клиентов"
            ),
            Project(
                id=2,
                title="Skateboard Shop",
                description="Интернет-магазин скейтбордов"
            )
        ]
    ),

    User(
        id=2,
        username="anna",
        email="anna@example.com",
        profile=Profile(
            first_name="Анна",
            last_name="Иванова",
            bio="Backend developer"
        ),
        projects=[
            Project(
                id=3,
                title="Travel App",
                description="Сервис для планирования путешествий"
            )
        ]
    ),

    User(
        id=3,
        username="alex",
        email="alex@example.com",
        profile=Profile(
            first_name="Алекс",
            last_name="Петров",
            bio="Fullstack developer"
        ),
        projects=[
            Project(
                id=4,
                title="Football Platform",
                description="Платформа для футбольных турниров"
            )
        ]
    )
]

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[User])
def get_users():
    return users_db

@router.get("/{user_id}",response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="user not found"
    )
@router.get("/{user_id}/profile",response_model=Profile)
def get_user_profile(user_id:int):
    for user in users_db:
        if user.id == user_id:
            return user.profile

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
