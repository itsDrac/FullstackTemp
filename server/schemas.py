from pydantic import BaseModel, field_validator

class CreateHero(BaseModel):
    name: str
    realName: str | None = None
    description: str

    @field_validator("name", "realName")
    @classmethod
    def make_title(cls, val):
        return val.title()
