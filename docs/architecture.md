# Data Quality Framework - Architecture Documentation

## System Overview

The Data Quality Validation Framework is a comprehensive, modular system designed to validate data quality across multiple dimensions before consumption by analytics modules.

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         Data Sources                             │
│  (CSV, JSON, SQL DB, APIs, IoT Streams, Third-party Feeds)      │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Ingestion Layer                          │
│        (Adapters: CSV, JSON, SQL, REST API)                      │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│              Rule Definition & Loading Engine                    │
│       (YAML/JSON config files, rule versioning)                  │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│           DQ Validation Execution Engine                         │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │   │
│  │ │Completeness │ │ Accuracy    │ │ Consistency │  ...     │   │
│  │ │  Validator  │ │  Validator  │ │  Validator  │          │   │
│  │ └─────────────┘ └─────────────┘ └─────────────┘          │   │
│  └───────────────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────────────┘
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     ▼               ▼               ▼
┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│ Scorecard   │ │  Quarantine  │ │   Lineage    │
│  Generator  │ │   Manager    │ │   Tracker    │
└─────────────┘ └──────────────┘ └──────────────┘
     │               │               │
     ▼               ▼               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Storage (PostgreSQL)                     │
│   (Scores, Quarantine Records, Lineage Graph, Rules)             │
└─────────────────────────────────────────────────────────────────┘
     │               │               │
     ▼               ▼               ▼
┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│   Alert     │ │ REST API     │ │ Frontend     │
│  System     │ │ (FastAPI)    │ │  Dashboard   │
└─────────────┘ └──────────────┘ └──────────────┘
```

## Backend Architecture

### Core Components

#### 1. Rule Definition Engine (`src/rules/`)
- **Responsibility**: Load, parse, and manage DQ validation rules
- **Key Classes**:
  - `RuleLoader`: Load YAML/JSON rule definitions
  - `RuleParser`: Parse and validate rule syntax
  - `RuleRegistry`: Maintain registry of active rules per module

#### 2. Validation Engine (`src/core/`)
- **Responsibility**: Execute validation checks and orchestrate validators
- **Key Classes**:
  - `Validator`: Main orchestrator
  - `ValidationEngine`: Execution logic
  - `ValidationResult`: Result data structure

#### 3. Dimension Validators (`src/validators/`)
- **Completeness Validator**: Check for null values and mandatory fields
- **Accuracy Validator**: Range checks, pattern matching, lookup validations
- **Consistency Validator**: Cross-source joins, referential integrity
- **Timeliness Validator**: Timestamp freshness checks
- **Uniqueness Validator**: Duplicate detection, primary key validation

#### 4. Quarantine Manager (`src/quarantine/`)
- **Responsibility**: Isolate failed records and maintain quarantine logs
- **Key Classes**:
  - `QuarantineManager`: Manage failed records
  - `QuarantineRecord`: Data model for quarantined records
  - `QuarantineAnalyzer`: Analyze failure patterns

#### 5. Data Lineage Tracker (`src/lineage/`)
- **Responsibility**: Build and visualize data flow DAGs
- **Key Classes**:
  - `LineageTracker`: Build lineage graphs
  - `LineageVisualizer`: Generate visual representations
  - `LineageNode`: Represents data processing nodes

#### 6. Alert System (`src/alerts/`)
- **Responsibility**: Monitor quality thresholds and notify stakeholders
- **Key Classes**:
  - `AlertManager`: Manage alert configurations
  - `Notifier`: Send email/log notifications
  - `ThresholdEvaluator`: Evaluate DQ score thresholds

#### 7. REST API (`src/api/`)
- **Framework**: FastAPI
- **Key Endpoints**:
  - `/validation/validate` - Run validation
  - `/validation/scorecards` - Get DQ scorecards
  - `/quarantine/records` - List quarantined records
  - `/lineage/graph` - Get data lineage
  - `/alerts/configure` - Configure alerts

### Database Schema

```sql
-- Rules Table
CREATE TABLE rules (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  dimension VARCHAR(50),
  module VARCHAR(255),
  definition JSONB,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- DQ Scores Table
CREATE TABLE dq_scores (
  id SERIAL PRIMARY KEY,
  source_name VARCHAR(255),
  module_name VARCHAR(255),
  completeness FLOAT,
  accuracy FLOAT,
  consistency FLOAT,
  timeliness FLOAT,
  uniqueness FLOAT,
  overall_score FLOAT,
  evaluated_at TIMESTAMP
);

-- Quarantine Table
CREATE TABLE quarantine (
  id SERIAL PRIMARY KEY,
  source_name VARCHAR(255),
  record_id VARCHAR(255),
  failing_rule_id INTEGER REFERENCES rules(id),
  record_data JSONB,
  failure_reason TEXT,
  quarantined_at TIMESTAMP
);

-- Lineage Table
CREATE TABLE lineage (
  id SERIAL PRIMARY KEY,
  source_node VARCHAR(255),
  target_node VARCHAR(255),
  transformation_type VARCHAR(100),
  created_at TIMESTAMP
);
```

## Frontend Architecture

### Component Hierarchy

```
App
├── Navigation
├── Dashboard Page
│   ├── KPI Cards
│   ├── Quality Trend Chart
│   └── Recent Issues Widget
├── Scorecards Page
│   ├── Dimension Cards
│   ├── Source Filter
│   └── Trend Chart
├── Quarantine Page
│   ├── Records Table
│   ├── Filter Panel
│   └── Detail Modal
├── Lineage Page
│   ├── DAG Visualization
│   └── Node Details
├── Alerts Page
│   ├── Alert List
│   ├── Alert Configuration Form
│   └── History
├── Rules Page
│   ├── Rule List
│   ├── Rule Editor
│   └── Versioning
└── Settings Page
    └── Configuration Options
```

### State Management

Using Zustand for lightweight state management:

```typescript
// Store structure
interface AppStore {
  // Validation data
  scorecards: Scorecard[]
  quarantineRecords: QuarantineRecord[]
  lineageGraph: LineageGraph

  // UI state
  loading: boolean
  error: string | null
  selectedModule: string

  // Actions
  fetchScorecards: () => Promise<void>
  fetchQuarantine: () => Promise<void>
  fetchLineage: () => Promise<void>
}
```

### API Service Layer

```typescript
// API client structure
export const api = {
  validation: {
    runValidation: (source: string) => Promise<ValidationResult>
    getScorecards: () => Promise<Scorecard[]>
    getHistory: (days: number) => Promise<HistoricalData[]>
  },
  quarantine: {
    getRecords: () => Promise<QuarantineRecord[]>
    resolveRecord: (id: string) => Promise<void>
  },
  lineage: {
    getGraph: () => Promise<LineageGraph>
    getNodeDetails: (nodeId: string) => Promise<NodeDetails>
  }
}
```

## Data Flow

### Validation Execution Flow

1. **Ingestion**: Data arrives from various sources
2. **Rule Loading**: Applicable validation rules are loaded from config
3. **Validation**: Each validator checks data against rules
4. **Scoring**: Dimension scores calculated
5. **Quarantine**: Failed records isolated
6. **Lineage**: Data flow tracked
7. **Scoring**: DQ scorecard generated
8. **Alerting**: Alerts triggered if thresholds exceeded
9. **Reporting**: Results available via API/Dashboard

### Real-Time Updates

- WebSocket connections for live dashboard updates
- Event-driven architecture for alert notifications
- Polling mechanism as fallback for browser compatibility

## Deployment Architecture

### Local Development

```
Local Machine
├── Backend (Python FastAPI)
│   ├── Port: 8000
│   └── Database: PostgreSQL / SQLite
└── Frontend (React/Vite)
    └── Port: 5173
```

### Production Scaling

- **Kubernetes** for container orchestration
- **Docker** for containerization
- **Apache Airflow** for workflow scheduling
- **Load Balancer** for backend API distribution

## Security Considerations

1. **Authentication**: JWT tokens for API access
2. **Authorization**: Role-based access control (RBAC)
3. **Data Protection**: Encryption at rest and in transit
4. **Audit Logging**: Track all validation operations
5. **Input Validation**: Strict validation on all inputs

## Performance Optimization

1. **Batch Processing**: Process data in configurable batches
2. **Caching**: Redis caching for frequent queries
3. **Indexing**: Database indexes on key fields
4. **Async Operations**: Non-blocking validation for large datasets
5. **Pagination**: API results paginated for efficient data transfer

---

**Last Updated**: June 2026