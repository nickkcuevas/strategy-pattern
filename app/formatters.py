"""
Data formatting module using Strategy Pattern.
"""
from .strategy import FORMATTERS


# ============================================
# Public API
# ============================================

def format_response(data: dict, format_type: str) -> str:
    """Format response using Strategy pattern."""
    strategy = FORMATTERS.get(format_type)
    if not strategy:
        raise ValueError(f"Unknown format: {format_type}")
    
    return strategy.format(data)


def get_content_type(format_type: str) -> str:
    """Get content type for a format."""
    strategy = FORMATTERS.get(format_type)
    if not strategy:
        raise ValueError(f"Unknown format: {format_type}")
    
    return strategy.content_type


def get_available_formats() -> list[str]:
    """Get list of available format types."""
    return list(FORMATTERS.keys())
