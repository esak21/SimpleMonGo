from enum import STRICT
from time import sleep
from typing import List
import json

from pydantic import BaseModel, ValidationError, Field , EmailStr, SecretStr, HttpUrl ,  model_validator, ValidationInfo, field_validator, computed_field
from datetime import datetime, UTC
from functools import partial
from typing import Literal, Annotated
from uuid import uuid4, UUID

from pydantic import ConfigDict

class user(BaseModel):
    """ User class """
    model_config = ConfigDict(populate_by_name=True, strict= True, extra='allow' , validate_assignment=True)

    user_id: UUID = Field(alias= "esakki_user_id" , default_factory=uuid4)
    user_name: Annotated[str, Field(min_length=3, max_length=255)]
    email: EmailStr
    website: HttpUrl | None = None
    password: SecretStr
    age: Annotated[int, Field(gt=18, le=120)]
    verified_at : datetime | None = None
    bio: str = ""
    is_active: bool = True
    first_name: str = ""
    last_name: str = ""
    followers_count: int = 0

    @field_validator("user_name")  # Field we want to validate
    @classmethod
    def validate_user_name(cls, col_value :str ) -> str :
        if not col_value.replace("_", "").isalnum():
            raise ValueError("User name must contain only letters and underscores")
        return col_value.lower()

    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, col_value:str | None) -> str | None:
        if col_value and not col_value.startswith(("https://", "http://")):
            return f"https://{col_value}"
        return col_value

    @computed_field
    @property
    def display_name(self) -> str :
        if self.first_name and self.last_name :
            return f"{self.first_name} {self.last_name}"
        return self.user_name

    @computed_field
    @property
    def is_influencer(self) -> bool :
        if self.followers_count > 10000 :
            return True
        return False





class BuggyModel(BaseModel):
    items: list[str] = []  # All instances point to this SAME list in memory
    created_at: datetime = datetime.now()

# # Create two separate objects
# user_a = BuggyModel()
# user_a.items.append("Laptop")
# print(f"User A items: {user_a}") # ['Laptop']
# print(f"User A items: {user_a.items}") # ['Laptop']
# sleep(30)
# user_b = BuggyModel()
#
# # Add an item to User A's list
# user_b.items.append("Python")
# print(f"User B items: {user_b}") # ['Laptop']  <-- THE BUG!
# print(f"User A items: {user_a.items}") # ['Laptop']

class comments(BaseModel):
    content: Annotated[str, Field(min_length=1, max_length=255)]
    created_at: datetime = Field(default_factory= lambda: datetime.now)
    likes: int = 0
    email: EmailStr


class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=255)]
    content: Annotated[str, Field(min_length=10, max_length=555)]
    author: user
    blog_comments: List[comments] = Field(default_factory= list)
    view_count: int = 0
    is_published: bool = False
    #created_at: datetime = Field(default_factory=  lambda: datetime.now(tz=UTC))
    created_at: datetime = Field(default_factory= partial(datetime.now, tz=UTC))
    status: Literal["draft", "published" , "Archived"] = "draft"
    tags: list[str] = Field(default_factory=list)

    slug : Annotated[str,Field(pattern=r"^[a-z0-9-]+$")]





esakki = user(
    user_name="Esakki",
    email= "esakki@gmail.com",
    age=49,
    password="@@@@@@@",
    website="esakki.com"
)
print(esakki)
print(esakki.model_dump_json(indent=2))


post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "user_name": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}


post = BlogPost(**post_data)

print(post)


# lets serialize the data
user_data = {
    "user_id": "3bc4bf25-1b73-44da-9078-f2bb310c7374",
    "user_name": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "age": 39,
    "password": "secret123",
}
user = user.model_validate_json(json.dumps(user_data))

print(user.model_dump_json(indent=2, by_alias=True, exclude={"password"}))


print(user.model_dump_json(indent=2, by_alias=True, include={"user_name" , "email"}))


user.email="esakki"

print(user)