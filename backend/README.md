# Backend - Data Quality Validation Engine

The backend is a Python-based validation engine that implements the core DQ validation logic, rule execution, quarantine mechanism, data lineage tracking, and alerting systems.

## 🏗️ Architecture

```
backend/
├── src/
│   ├── core/              # Core validation engine
│   │   ├── __init__.py
│   │   ├── validator.py   # Main validator orchestrator
│   │   └── engine.py      # Validation execution engine
│   │
│   ├── rules/             # Rule definitions and loaders
│   │   ├── __init__.py
│   │   ├── loader.py      # Load rules from YAML/JSON
│   │   ├── parser.py      # Parse rule configurations
│   │   └── registry.py    # Rule registry
│   │
│   ├── validators/        # Dimension-specific validators
│   │   ├── __init__.py
│   │   ├── completeness.py    # Completeness checks
│   │   ├── accuracy.py        # Accuracy checks
│   │   ├── consistency.py     # Consistency checks
│   │   ├── timeliness.py      # Timeliness checks
│   │   └── uniqueness.py      # Uniqueness checks
│   │
│   ├── quarantine/        # Quarantine mechanism
│   │   ├── __init__.py
│   │   ├── manager.py     # Quarantine record manager
│   │   └── models.py      # Data models for quarantine
│   │
│   ├── lineage/           # Data lineage tracking
│   │   ├── __init__.py
│   │   ├── tracker.py     # Lineage graph builder
│   │   └── visualizer.py  # DAG visualization
│   │
│   ├── alerts/            # Alert and notification system
│   │   ├── __init__.py
│   │   ├── notifier.py    # Email/log notifications
│   │   └── thresholds.py  # Alert threshold logic
│   │
│   ├── database/          # Database models and ORM
│   │   ├── __init__.py
│   │   ├── models.py      # SQLAlchemy models
│   │   ├── connection.py  # DB connection management
│   │   └── migrations/    # Database migrations
│   │
│   ├── api/               # REST API endpoints
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI app initialization
│   │   ├── endpoints/
│   │   │   ├── validation.py
│   │   │   ├── scorecards.py
│   │   │   ├── quarantine.py
│   │   │   ├── lineage.py
│   │   │   └── health.py
│   │   └── schemas.py     # Pydantic schemas
│   │
│   ├── utils/             # Utility functions
│   │   ├── __init__.py
│   │   ├── logger.py      # Logging configuration
│   │   └── helpers.py     # Helper functions
│   │
│   └── config.py          # Configuration management
│
├── config/                # Configuration files
│   ├── rules/
│   │   ├── source1_rules.yaml
│   │   ├── source2_rules.yaml
│   │   └── ...
│   └── settings.yaml      # Global settings
│
├── tests/
│   ├── __init__.py
│   ├── test_validators.py
│   ├── test_rules.py
│   ├── test_quarantine.py
│   ├── test_api.py
│   └── fixtures/          # Test data
│
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip package manager

### Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Backend

```bash
# Development mode with auto-reload
python -m uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Alternative Docs: `http://localhost:8000/redoc`

## 🔧 Configuration

Configuration is managed through environment variables and files in `config/`:

```bash
# Set environment variables
export DATABASE_URL=postgresql://user:password@localhost:5432/dq_framework
export LOG_LEVEL=INFO
export ENV=development
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export SMTP_USERNAME=your_email@gmail.com
export SMTP_PASSWORD=your_app_password
```

Or create a `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/dq_framework
LOG_LEVEL=INFO
ENV=development
DEBUG=False
```

## 📦 Dependencies

Key Python packages:
- `fastapi` - Modern web framework
- `uvicorn` - ASGI server
- `sqlalchemy` - ORM
- `pandas` - Data processing
- `great-expectations` - Validation library
- `pydantic` - Data validation
- `networkx` - Graph operations
- `plotly` - Visualization
- `loguru` - Logging
- `pytest` - Testing

See `requirements.txt` for complete list.

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_validators.py -v
```

## 📝 Code Style

```bash
# Format code with black
black src/

# Check with flake8
flake8 src/

# Type checking with mypy
mypy src/

# Sort imports
isort src/
```

## 🔌 API Endpoints

### Validation
- `POST /validation/validate` - Run validation on data
- `GET /validation/scorecards` - Get DQ scorecards
- `GET /validation/history` - Get historical data

### Quarantine
- `GET /quarantine/records` - List quarantined records
- `POST /quarantine/resolve` - Mark record as resolved
- `DELETE /quarantine/:id` - Delete quarantine record

### Lineage
- `GET /lineage/graph` - Get data lineage DAG
- `GET /lineage/node/:id` - Get node details

### Alerts
- `GET /alerts/list` - List active alerts
- `POST /alerts/configure` - Configure alert thresholds
- `GET /alerts/history` - Alert history

### Health
- `GET /health` - Health check endpoint
- `GET /` - API info

## 📚 Documentation

- [Architecture](../docs/architecture.md)
- [API Documentation](../docs/api.md)
- [Rules Guide](../docs/rules-guide.md)

---

**Status**: Under Development | **Last Updated**: June 2026