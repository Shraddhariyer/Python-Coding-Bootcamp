from fastapi import FastAPI
from routers import notes
from models.note import init_db
app=FastAPI()
app.include_router(notes.router)
@app.get("/")
def root():
    return {"message":"Notes"}

@app.on_event("startup")
def startup():
    init_db