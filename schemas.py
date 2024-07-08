from pydantic import BaseModel


class Interactions(BaseModel):
    id: int
    input: str
    output: str
    metric: int
    class Config:
        orm_mode = True


class CreateLog(Interactions):
    class Config:
        orm_mode = True
