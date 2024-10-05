from fastapi import FastAPI
from app.routers import auth, therapy

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(therapy.router)


@app.get("/")
def read_root():
    return {"message": "Mental Health DAO Platform"}
