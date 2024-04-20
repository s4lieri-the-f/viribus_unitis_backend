from fastapi import FastAPI

app = FastAPI()
print("[INIT] INITIATED WEB-SERVER.")

@app.get("/")
async def root():
    return {"message": "Hello World"}