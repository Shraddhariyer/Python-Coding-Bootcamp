from fastapi import FastAPI, Request
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.middleware("http")
async def log_requests(request:Request, call_next):
    current_time=datetime.now().strftime("%H:%M:%S")
    print(current_time,request.method, request.url.path)
    response=await call_next(request)
    return response


@app.get("/")
def home():
    return{
        "message":"Visitor Logger"
    }

@app.get("/about")
def about():
    return{
        "message":"About Page"
    }