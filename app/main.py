from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ArtCommision API")

app.add_middleware(
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="ArtCommision API")

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

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
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
        "supported_roles": ["artist", "client"],
        "service_types": [
            "Character Design",
            "Illustration",
            "Animation",
            "Logo Design",
            "Custom Artwork"
        ],
        "version": "1.0",
        "contact": {
            "developer": "Rafidhiyaulhaq",
            "email": "your.email@example.com",
            "github": "https://github.com/rafidhiyaulhaq"
        },
        "documentation": "/docs"
    }

@app.get("/api/sample-services")
def get_sample_services():
    return {
        "services": [
            {
                "type": "Character Design",
                "price_range": {
                    "basic": "Rp 200.000",
                    "standard": "Rp 350.000",
                    "premium": "Rp 500.000"
                },
                "delivery_time": "3-7 days"
            },
            {
                "type": "Illustration",
                "price_range": {
                    "basic": "Rp 300.000",
                    "standard": "Rp 450.000",
                    "premium": "Rp 650.000"
                },
                "delivery_time": "5-10 days"
            }
        ],
        "note": "Harga dapat berbeda tergantung kompleksitas dan kebutuhan spesifik"
    }    CORSMiddleware,
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

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ArtCommision API"
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
