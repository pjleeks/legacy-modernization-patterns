from fastapi import FastAPI
from src.core.processing import calculate_total

app = FastAPI()

@app.post("/calculate")
def calculate(data: list[float]):
    return {"result": calculate_total(data)}

