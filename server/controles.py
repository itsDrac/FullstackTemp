from sqlmodel import Session, select
from models import Hero as HeroModel
from schemas import CreateHero as CreateHeroSchema

import errors

async def add_hero(hero: CreateHeroSchema, db: Session):
    statement = select(HeroModel).where(HeroModel.name == hero.name)
    existHero = db.exec(statement).one_or_none()
    if existHero:
        raise errors.AlreadyExist(msg=f"Hero with name {hero.name} already exist")
    newHero = HeroModel(**hero.model_dump())
    db.add(newHero)
    db.commit()
    return {"message": "Hero added successfuly"}
