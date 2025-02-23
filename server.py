from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from routes.userRoutes import router as user_router
import os

app = FastAPI()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")


db_client = AsyncIOMotorClient(MONGO_URI)
db = db_client.mydatabase


app.include_router(user_router, prefix="/api")


@app.middleware("http")
async def db_session_middleware(request, call_next):
    response = await call_next(request)
    db_client.close()
    return response
