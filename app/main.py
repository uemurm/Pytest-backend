from fastapi import FastAPI, HTTPException
from app.schemas import UserCreate, UserUpdate, User

app = FastAPI(title="Do Pytest Backend")

users_store = {}    # Be aware that this is not a list but a dictionary.
next_id = 1


@app.post("/users", status_code=201, response_model=User)
def create_user(user: UserCreate):
    global next_id
    user_id = next_id
    next_id += 1

    new_user = User(
        id=user_id,
        name=user.name,
        email=user.email,
        age=user.age
    )
    users_store[user_id] = new_user
    return new_user


@app.get("/users", response_model=list[User])
def list_users():
    return list(users_store.values())


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users_store:
        raise HTTPException(status_code=404, detail="User not found")
    return users_store[user_id]


@app.patch("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_store:
        raise HTTPException(status_code=404, detail="User not found")

    user = users_store[user_id]
    update_data = user_update.dict(exclude_unset=True)
    updated_user = user.copy(update={**update_data})
    users_store[user_id] = updated_user
    return updated_user


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users_store:
        raise HTTPException(status_code=404, detail="User not found")
    del users_store[user_id]
    return None
