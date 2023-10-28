from fastapi import FastAPI
try:
    from models.post import UserPost,post_item
except Exception as e:
    from app.models.post import UserPost,post_item
from fastapi.responses import JSONResponse
import json
import sqlalchemy
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
# from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine


app=FastAPI()
headers = {'Access-Control-Allow-Origin': '*',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*'
        }
origins=['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def hello():
    res={"message":"Hello 28 oct"}
    return JSONResponse(res, status_code=200, headers=headers)


@app.post("/savedetails")
async def savedetails(post:UserPost):
    try:
    
        msg=  "Hi "+post.first_name.title() +",Thanks for submitting your feedback!"+" See you again."
        response={"message":msg,"code":"200"}
        return JSONResponse(dict(response), status_code=200, headers=headers)
    except Exception as e:
        return JSONResponse({"message":str(e),"code":"500"},status_code=500, headers=headers)
    # headers['content-type']='application/json'
    

@app.post("/saveitems")
async def postitem(post:post_item):
    
    return JSONResponse(post, status_code=200, headers=headers)



# def insert_predlog():
#   ssh_tunnel = SSHTunnelForwarder(
#                   '18.144.161.193',
#                   ssh_username='ec2-user',
#                   ssh_private_key= 'db-key.pem',
#                   remote_bind_address=('meetup-rds.cclbxzdtfauu.us-west-1.rds.amazonaws.com', 5432)
#               )
#   ssh_tunnel.start()
#   # engine = create_engine(f"postgresql+psycopg2://impuser:ImpU53r%40123@sdq-v2-ga-ops-dev.c1exmwlyuhyt.us-east-1.rds.amazonaws.com:{ssh_tunnel.local_bind_port}/sdq-int2")
#   engine=create_engine(f"postgresql+psycopg2://postgres:Admin123@meetup-rds.cclbxzdtfauu.us-west-1.rds.amazonaws.com:{ssh_tunnel.local_bind_address}/postgres'")
#   return engine.connect()
