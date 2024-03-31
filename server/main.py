from fastapi import FastAPI, Depends, HTTPException, Request
from sqlmodel import Session
from models import Hero as HeroModel
from schemas import CreateHero as CreateHeroSchema
from fastapi.middleware.cors import CORSMiddleware
import database, controles as c, errors
from pydantic import BaseModel, field_validator

app = FastAPI()
app.add_middleware(
        CORSMiddleware, 
        allow_origins=["http://localhost:3000", "frontend:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )

@app.on_event("startup")
async def startup():
    database.create_metadata()

@app.get("/ping")
async def pong():
    return {"message": "Pong"}

class Test(BaseModel):
    name: str

@app.post("/test")
async def test(item:CreateHeroSchema):
    print(item)
    return {"received_data": item.name}

@app.post("/create")
async def hero(req: Request, details: CreateHeroSchema, db: Session = Depends(database.get_session)):
    print(details)
    result = {}
    try:
        result = await c.add_hero(details, db)
    except errors.AlreadyExist as err:
        print(err.message)
        raise HTTPException(403, err.message)

    return result
