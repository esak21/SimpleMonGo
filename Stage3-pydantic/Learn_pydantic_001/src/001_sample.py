def create_user(user_name, email, age):
    if not isinstance(age, int):
        raise TypeError("Age must be integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if not isinstance(user_name, str):
        raise TypeError("User name must be string")
    if not isinstance(email, str):
        raise TypeError("Email must be string")


# user1 = create_user("esakki", "essaki@gmail.com", 33)
# print(user1)
#
# user3 = create_user("esakki2", None, 10)
# print(user3)
#
#
# user2 = create_user("esakki2", "essaki@gmail.com", -1)
# print(user2)


from pydantic import BaseModel
class User(BaseModel):
    user_name: str
    email: str
    age: int


user_pydantic_1 = User(user_name="esakki", email="essaki@gmail.com", age=33)
print(user_pydantic_1)
user_pydantic_2 = User(user_name="esakki", email="essaki@gmail.com", age=-1)
print(user_pydantic_2)
user_pydantic_3 = User(user_name="esakki", email= None, age=33)
print(user_pydantic_3)