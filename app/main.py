from fastapi import FastAPI

from app.api.routes import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the GenAI Assistant API!"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=3001)
