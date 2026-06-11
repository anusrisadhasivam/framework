"""
Utility Functions.
"""

from datetime import datetime, timedelta

def format_date(date_obj):
    """
    Format date object to string.
    
    Args:
        date_obj: Date object
    
    Returns:
        Formatted date string
    """
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

def get_date_range(days: int = 7):
    """
    Get date range for the last N days.
    
    Args:
        days: Number of days
    
    Returns:
        Tuple of (start_date, end_date)
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return start_date, end_date

def format_number(value: float, decimals: int = 2) -> str:
    """
    Format number with specified decimal places.
    
    Args:
        value: Number to format
        decimals: Number of decimal places
    
    Returns:
        Formatted number string
    """
    return f"{value:.{decimals}f}"

def get_severity_color(severity: str) -> str:
    """
    Get color for severity level.
    
    Args:
        severity: Severity level (critical, warning, info)
    
    Returns:
        Color code
    """
    colors = {
        'critical': '#ef4444',
        'warning': '#f59e0b',
        'info': '#0ea5e9',
    }
    return colors.get(severity.lower(), '#808080')