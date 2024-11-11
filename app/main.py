from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, users, portfolio, orders, progress
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ArtCommission API")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(portfolio.router)
app.include_router(orders.router)
app.include_router(progress.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ArtCommission API"}