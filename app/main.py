from fastapi import FastAPI
from models.post import UserPost

app=FastAPI()

@app.get("/health")
async def hello():
    return {"message":"hello world"}

@app.post("/savedetails")
async def savedetails(post:UserPost):
    return post.name + post.gender