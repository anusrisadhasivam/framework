"""
Configuration management for the DQ Validation Framework backend.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://dq_user:dq_password@localhost:5432/dq_framework"
    )

    # API
    API_TITLE: str = "Data Quality Validation Framework"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = "Comprehensive automated data quality validation engine"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "json"

    # Environment
    ENV: str = os.getenv("ENV", "development")

    # Alerts
    SMTP_SERVER: Optional[str] = os.getenv("SMTP_SERVER")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USERNAME: Optional[str] = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD: Optional[str] = os.getenv("SMTP_PASSWORD")
    ALERT_EMAIL_FROM: Optional[str] = os.getenv("ALERT_EMAIL_FROM")
    ALERT_EMAIL_TO: Optional[list] = None

    # Validation
    DEFAULT_BATCH_SIZE: int = 10000
    DEFAULT_ALERT_THRESHOLD: float = 0.8  # 80%

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()