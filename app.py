from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated
import datetime

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str

repo = []

app = FastAPI()

@app.get("/orders")
def get_orders():
    return repo

@app.post("/orders")
def create_order(dto: Annotated[Order, Form()]):
    repo.append(dto)
    return {"message": "Order created successfully"}
