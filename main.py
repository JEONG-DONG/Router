from fastapi import FastAPI
from routes import item, users

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

app.include_router(item.router)
app.include_router(users.router)
