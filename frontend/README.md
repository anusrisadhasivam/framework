# Frontend - Data Quality Dashboard (Dash/Plotly)

A Python-based web application using Plotly/Dash for monitoring, analyzing, and managing data quality validation results.

## 🎨 Features

- **Real-time DQ Scorecards**: Monitor quality scores across all dimensions
- **Interactive Dashboards**: Visualize validation results with Plotly charts
- **Quarantine Management**: Review and manage quarantined records
- **Data Lineage Visualization**: Explore data flow through the pipeline
- **Alert Management**: Configure and monitor data quality alerts
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Real-time Updates**: Live data refresh with WebSocket support

## 🏗️ Project Structure

```
frontend/
├── src/
│   ├── app.py              # Main Dash application
│   ├── callbacks.py        # Dash callbacks and interactivity
│   │
│   ├── layouts/            # Page layouts
│   │   ├── dashboard.py    # Main dashboard layout
│   │   ├── scorecards.py   # DQ scorecards layout
│   │   ├── quarantine.py   # Quarantine records layout
│   │   ├── lineage.py      # Data lineage layout
│   │   └── alerts.py       # Alerts management layout
│   │
│   ├── components/         # Reusable Dash components
│   │   ├── charts.py       # Chart components
│   │   ├── tables.py       # Table components
│   │   └── graphs.py       # Graph visualization components
│   │
│   ├── services/
│   │   └── api_client.py   # API client for backend
│   │
│   └── utils.py            # Utility functions
│
├── assets/                 # CSS and static files
│   ├── style.css           # Custom styling
│   └── favicon.ico         # Favicon
│
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Backend API running on `http://localhost:8000`

### Installation

```bash
cd frontend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Dashboard

```bash
python src/app.py
```

The dashboard will be available at `http://localhost:8050`

## 📦 Dependencies

Key Python packages:
- `dash` - Interactive web framework
- `plotly` - Interactive visualization library
- `pandas` - Data processing and analysis
- `requests` - HTTP client for API calls
- `networkx` - Graph operations for lineage
- `python-dateutil` - Date/time utilities

See `requirements.txt` for complete list.

## 🔌 API Integration

The frontend communicates with the backend API:

```python
from src.services.api_client import APIClient

client = APIClient('http://localhost:8000')

# Get DQ scorecards
scorecards = client.get_scorecards()

# Get quarantined records
quarantine_records = client.get_quarantine_records()

# Get data lineage
lineage = client.get_lineage_graph()
```

## 🎯 Key Pages

- **Dashboard**: Overview of all DQ metrics with key performance indicators
- **Scorecards**: Detailed quality scores per dimension and per source
- **Quarantine**: View and manage failed records
- **Lineage**: Visualize data flow through the pipeline
- **Alerts**: Configure and monitor data quality alerts

## 📊 Visualization Components

### Charts
- **Time Series Charts**: Track quality scores over time
- **Bar Charts**: Compare scores across dimensions
- **Gauge Charts**: Show current quality status
- **Pie Charts**: Distribution of data quality issues

### Tables
- **Quarantine Records Table**: Display failed records with details
- **Alerts Table**: Show active and historical alerts
- **Lineage Table**: Display data flow relationships

### Graphs
- **Lineage DAG**: Visualize data flow as directed acyclic graph
- **Network Graph**: Show relationships between data sources

## 🌐 Environment Variables

Create a `.env` file in the frontend directory:

```env
BACKEND_API_URL=http://localhost:8000
DASH_DEBUG=True
DASH_HOT_RELOAD=True
```

## 🧪 Testing

```bash
python -m pytest tests/
```

## 📝 Code Style

```bash
# Format code with black
black src/

# Check with flake8
flake8 src/

# Type checking with mypy
mypy src/
```

## 📚 Additional Resources

- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Documentation](https://plotly.com/python/)
- [Python Documentation](https://docs.python.org/3/)

---

**Status**: Under Development | **Last Updated**: June 2026