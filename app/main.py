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
        "service": "ArtCommision API"
    }