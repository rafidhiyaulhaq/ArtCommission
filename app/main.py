from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ArtCommision API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "project": "ArtCommision API",
        "version": "1.0",
        "developer": "Rafidhiyaulhaq",
        "description": "Platform manajemen pesanan karya seni digital"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ArtCommision API",
        "environment": "production"
    }

@app.get("/api/info")
def get_api_info():
    return {
        "name": "ArtCommision API",
        "features": [
            "Digital Art Commission Management",
            "Artist Portfolio System",
            "Order Management",
            "Progress Tracking"
        ],
        "version": "1.0",
        "contact": {
            "developer": "Rafidhiyaulhaq",
            "email": "rafidhiyaulhaq.m@gmail.com"
        }
    }