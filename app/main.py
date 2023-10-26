from fastapi import FastAPI
from models.post import UserPost
from fastapi.responses import JSONResponse


app=FastAPI()
headers = {'Access-Control-Allow-Origin': '*',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*'
        }

@app.get("/health")
async def hello():
    res={"message":"hello world"}
    return JSONResponse(res, status_code=200, headers=headers)

@app.post("/savedetails")
async def savedetails(post:UserPost):
    # print(post)
    return JSONResponse(post, status_code=200, headers=headers)
        
        
       

