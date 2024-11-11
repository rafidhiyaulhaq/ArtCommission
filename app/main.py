from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from enum import Enum
from datetime import datetime
from pydantic import BaseModel

app = FastAPI(
    title="ArtCommision API",
    description="Platform manajemen pesanan karya seni digital",
    version="1.0",
    contact={
        "name": "Rafidhiyaulhaq",
        "email": "your.email@example.com"
    }
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enums for standardization
class ArtStyle(str, Enum):
    ANIME = "anime"
    REALISTIC = "realistic"
    CARTOON = "cartoon"
    CHIBI = "chibi"
    PIXEL_ART = "pixel_art"

class OrderStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    REVISION = "revision"
    COMPLETED = "completed"

# Pydantic models
class ServicePrice(BaseModel):
    basic: str
    standard: str
    premium: str

class ArtService(BaseModel):
    style: ArtStyle
    price_range: ServicePrice
    delivery_time: str
    revisions: int

# Sample data
SERVICES = {
    ArtStyle.ANIME: ArtService(
        style=ArtStyle.ANIME,
        price_range=ServicePrice(
            basic="Rp 200.000",
            standard="Rp 350.000",
            premium="Rp 500.000"
        ),
        delivery_time="3-7 days",
        revisions=2
    ),
    ArtStyle.REALISTIC: ArtService(
        style=ArtStyle.REALISTIC,
        price_range=ServicePrice(
            basic="Rp 400.000",
            standard="Rp 650.000",
            premium="Rp 900.000"
        ),
        delivery_time="5-10 days",
        revisions=3
    )
}

@app.get("/")
def read_root():
    return {
        "project": "ArtCommision API",
        "version": "1.0",
        "developer": "Rafidhiyaulhaq",
        "description": "Platform manajemen pesanan karya seni digital",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ArtCommision API",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0"
    }

@app.get("/api/styles")
def get_art_styles():
    return {
        "available_styles": [style.value for style in ArtStyle],
        "description": "List of available art styles for commission"
    }

@app.get("/api/services/{style}")
def get_service_details(style: ArtStyle):
    if style not in SERVICES:
        raise HTTPException(status_code=404, detail="Art style not found")
    return SERVICES[style]

@app.get("/api/services")
def get_services(
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    style: Optional[ArtStyle] = Query(None, description="Filter by art style")
):
    filtered_services = SERVICES
    if style:
        filtered_services = {k: v for k, v in SERVICES.items() if k == style}
    return {
        "services": filtered_services,
        "total": len(filtered_services),
        "filters_applied": {
            "min_price": min_price,
            "style": style.value if style else None
        }
    }

@app.get("/api/example-order")
def get_example_order():
    return {
        "order_id": "ORD001",
        "style": ArtStyle.ANIME,
        "description": "Full body character illustration, anime style",
        "references": ["url1", "url2"],
        "status": OrderStatus.IN_PROGRESS,
        "timeline": {
            "ordered_at": "2024-03-12T10:00:00",
            "started_at": "2024-03-12T14:00:00",
            "estimated_completion": "2024-03-15T14:00:00"
        },
        "price_tier": "standard",
        "revisions_left": 2
    }

@app.get("/api/features")
def get_features():
    return {
        "current_features": [
            {
                "name": "Art Style Selection",
                "description": "Choose from various art styles",
                "endpoint": "/api/styles"
            },
            {
                "name": "Service Details",
                "description": "Get detailed information about services",
                "endpoint": "/api/services/{style}"
            },
            {
                "name": "Price Filtering",
                "description": "Filter services by price range",
                "endpoint": "/api/services?min_price={value}"
            }
        ],
        "upcoming_features": [
            "Real-time Progress Tracking",
            "Integrated Payment System",
            "Artist Portfolio Management",
            "Review and Rating System"
        ]
    }