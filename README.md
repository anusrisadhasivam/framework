# Data Quality (DQ) Validation Framework

A comprehensive, automated solution that validates data feeding into analytics modules before any downstream processing occurs. The framework acts as a gatekeeper, ensuring that all data consumed by reporting, forecasting, and AI modules meets defined quality standards.

## 🎯 Project Overview

This project proposes the design and implementation of a Data Quality (DQ) Validation Framework covering five core quality dimensions:
- **Completeness**: All required fields are populated with non-null values
- **Accuracy**: Data correctly represents the real-world entity or event
- **Consistency**: Data is uniform and non-contradictory across all sources
- **Timeliness**: Data is current and within acceptable freshness windows
- **Uniqueness**: No duplicate records exist within or across data sets

## 📁 Project Structure

```
framework/
├── backend/                 # Python backend validation engine
│   ├── src/
│   │   ├── core/           # Core validation engine
│   │   ├── rules/          # Rule definitions and loaders
│   │   ├── validators/     # Validation implementations
│   │   ├── quarantine/     # Quarantine mechanism
│   │   ├── lineage/        # Data lineage tracking
│   │   ├── alerts/         # Alerting system
│   │   ├── database/       # Database models
│   │   ├── api/            # REST API endpoints
│   │   └── utils/          # Utility functions
│   ├── config/             # Configuration files (YAML/JSON)
│   ├── tests/              # Unit and integration tests
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
│
├── frontend/               # Python Dash/Plotly dashboard
│   ├── src/
│   │   ├── app.py          # Main Dash application
│   │   ├── callbacks.py    # Dash callbacks and interactivity
│   │   ├── layouts/        # Page layouts
│   │   │   ├── dashboard.py
│   │   │   ├── scorecards.py
│   │   │   ├── quarantine.py
│   │   │   ├── lineage.py
│   │   │   └── alerts.py
│   │   ├── components/     # Reusable Dash components
│   │   │   ├── charts.py
│   │   │   ├── tables.py
│   │   │   └── graphs.py
│   │   ├── services/       # API client for backend
│   │   └── utils.py        # Utility functions
│   ├── assets/             # CSS and static assets
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Frontend documentation
│
├── docs/                   # Project documentation
│   ├── architecture.md     # System architecture
│   ├── api.md              # API documentation
│   └── rules-guide.md      # Rule definition guide
│
├── .gitignore              # Git ignore rules
├── LICENSE                 # License file
└── README.md              # This file

```

## 🔧 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|----------|
| **Language** | Python 3.10+ | Backend & Frontend |
| **Validation Library** | Great Expectations / Pandas | Rule assertion and checks |
| **Database** | PostgreSQL / SQLite | Storing results and quarantine records |
| **Orchestration** | Apache Airflow / Cron | Scheduling batch validation runs |
| **Visualization** | Plotly / Dash | DQ scorecard dashboards |
| **Lineage Graph** | NetworkX / Graphviz | Data lineage DAG rendering |
| **Configuration** | YAML / JSON | Rule definitions and thresholds |
| **Alerting** | Python smtplib / Loguru | Email alerts and structured logging |
| **API Framework** | FastAPI | RESTful API for backend services |
| **Web Framework** | Dash | Interactive web dashboards |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL 12+ or SQLite (Database)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn src.api.main:app --reload
```

### Frontend Setup

```bash
cd frontend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py  # Runs on http://localhost:8050
```

### Access the Application
- Frontend Dashboard: `http://localhost:8050`
- Backend API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

## 📊 Key Features

1. **Rule-Based Validation Engine**: Configuration-driven rules for each data source
2. **Automated Validation Checks**: Comprehensive checks across all five quality dimensions
3. **Real-Time DQ Scorecards**: Per-source and per-module quality metrics
4. **Quarantine Mechanism**: Automatic isolation of failing records
5. **Data Lineage Tracking**: Full traceability from source to output
6. **Automated Alerts**: Email and log-based notifications
7. **Interactive Dashboards**: Web-based UI using Plotly/Dash
8. **Extensible Architecture**: Reusable framework for all analytics modules

## 📚 Documentation

- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)
- [Architecture Guide](./docs/architecture.md)
- [API Documentation](./docs/api.md)
- [Rule Definition Guide](./docs/rules-guide.md)

## 🤝 Contributing

Contributions are welcome! Please refer to the contributing guidelines in each module's README.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 📞 Support

For issues, questions, or feature requests, please open an issue on GitHub or contact the project maintainers.

---

**Status**: Under Development | **Last Updated**: June 2026