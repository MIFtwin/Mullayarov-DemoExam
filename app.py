from datetime import date
from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form

app = FastAPI()

class Order(BaseModel):
    number: int
    startDate: date  # Обратите внимание на имя поля и тип
    device: str
    problemType: str
    description: str
    client: str
    status: str

# Пример данных
repo = [
    Order(
        number=1,
        startDate="2024-11-14",  # Передаем как строку, Pydantic автоматически преобразует
        device="123",
        problemType="345",
        description="678",
        client="Ил",
        status="В ожидании"
    )
]

# Эндпоинт для отображения данных из repo
@app.get("/orders")
def get_orders():
    return repo


@app.post("/orders")
def create_order(dto : Annotated[Order,  Form()]):
    repo.append(dto)





 
app = FastAPI()
 
@app.get("/orders")
def get_orders():
    
    return repo