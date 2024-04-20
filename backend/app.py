from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"{randint(0, 1488)}"}