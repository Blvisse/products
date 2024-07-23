from fastapi import FastAPI
from scripts.add import quick_addition

app = FastAPI()


@app.get("/sum")
async def addition_endpoint():
    result = quick_addition(1, 2, 3)
    return {"hello": "world",
            "results": result}


@app.get("/")
async def home():
    return {"hello": "world"}
