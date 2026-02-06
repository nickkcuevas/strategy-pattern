"""
API endpoints for data formatting.
"""
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import Response
from .formatters import format_response, get_content_type, get_available_formats

router = APIRouter()


@router.get("/api/data")
async def get_data(format: str = Query("json")):
    """Get data in specified format."""
    # Validate format
    if format not in get_available_formats():
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format. Available: {', '.join(get_available_formats())}"
        )
    
    data = {"name": "John", "age": 30, "city": "NYC"}
    
    # Format using strategy
    formatted = format_response(data, format)
    
    # Get content type from strategy
    content_type = get_content_type(format)
    
    return Response(content=formatted, media_type=content_type)


@router.get("/api/formats")
async def list_formats():
    """List all available formats."""
    return {"formats": get_available_formats()}
