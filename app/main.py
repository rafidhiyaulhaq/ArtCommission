from fastapi import FastAPI

app = FastAPI(title="ArtCommision API")

@app.get("/")
def read_root():
    return {
        "project": "ArtCommision API",
        "version": "1.0",
        "developer": "Rafidhiyaulhaq",
        "description": "Platform manajemen pesanan karya seni digital"
    }

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ArtCommision API"
    }