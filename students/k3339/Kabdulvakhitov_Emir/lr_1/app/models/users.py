from pydantic import BaseModel

class Profile(BaseModel):
    first_name: str
    last_name: str
    bio: str

class Project(BaseModel):
    id: int
    title: str
    description: str

class User(BaseModel):
    id: int
    username: str
    email: str
    profile: Profile
    projects: list[Project]