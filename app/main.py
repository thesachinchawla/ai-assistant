from fastAPI import FastAPI
from app.api.routes import router

app = FastAPI()


app.include_router(router, prefix="/api/v1/")

@app.get("/")
async def root():
    return {"message": "Welcome to the GenAI Assistant API!"}

