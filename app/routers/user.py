from fastapi import APIRouter, Depends, status
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session

# # Using Router 
router = APIRouter()

@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateUser)
def create_user(user: schemas.CreateUser, db:Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    
    # Saving data to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user    