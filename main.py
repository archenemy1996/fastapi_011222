from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI() # Create an instance for FasatAPI

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = []

@app.get("/")
def root():
    return("messsage": "Hello World")



@app.get("/posts")
def get_posts():
    return("data": "This is da post")


    


