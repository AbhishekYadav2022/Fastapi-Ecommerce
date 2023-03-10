from fastapi import FastAPI
from . import models
from .routers import user
from .database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# For Testing Purpose 
@app.get("/")
def root():
    return {"message": "success!"}

app.include_router(user.router)