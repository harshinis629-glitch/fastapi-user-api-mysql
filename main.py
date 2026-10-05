from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles

from database import SessionLocal
from models import User
from schemas import UserCreate, UserResponse

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "User API is running"}


# CREATE USER
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        id=str(__import__("uuid").uuid4()),
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# GET ALL USERS
@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    return db.query(User).all()


# GET ONE USER
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# UPDATE USER
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: str,
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.name = user_data.name
    user.email = user_data.email
    user.age = user_data.age

    db.commit()
    db.refresh(user)

    return user


# DELETE USER
@app.delete("/users/{user_id}")
def delete_user(
    user_id: str,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }