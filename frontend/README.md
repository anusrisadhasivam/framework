# Frontend - Data Quality Dashboard

A modern, responsive React + TypeScript web application for monitoring, analyzing, and managing data quality validation results.

## 🎨 Features

- **Real-time DQ Scorecards**: Monitor quality scores across all dimensions
- **Interactive Dashboards**: Visualize validation results with Plotly charts
- **Quarantine Management**: Review and manage quarantined records
- **Data Lineage Visualization**: Explore data flow through the pipeline
- **Alert Management**: Configure and monitor data quality alerts
- **Rule Management**: View, create, and edit validation rules
- **Historical Analysis**: Track quality trends over time

## 🏗️ Project Structure

```
frontend/
├── src/
│   ├── components/        # Reusable React components
│   │   ├── common/        # Common components (Header, Footer, etc.)
│   │   ├── dashboard/     # Dashboard-specific components
│   │   ├── charts/        # Chart components
│   │   ├── forms/         # Form components
│   │   └── layout/        # Layout components
│   │
│   ├── pages/             # Page components
│   │   ├── Dashboard.tsx
│   │   ├── Scorecards.tsx
│   │   ├── Quarantine.tsx
│   │   ├── Lineage.tsx
│   │   ├── Alerts.tsx
│   │   ├── Rules.tsx
│   │   └── Settings.tsx
│   │
│   ├── services/          # API client services
│   │   ├── api.ts         # API base client
│   │   ├── validation.ts  # Validation API calls
│   │   ├── scorecards.ts  # Scorecard API calls
│   │   └── quarantine.ts  # Quarantine API calls
│   │
│   ├── store/             # State management (Zustand)
│   │   ├── store.ts
│   │   ├── slices/
│   │   └── hooks.ts
│   │
│   ├── styles/            # Global styles
│   │   ├── index.css
│   │   ├── variables.css
│   │   └── theme.css
│   │
│   ├── types/             # TypeScript type definitions
│   │   └── index.ts
│   │
│   ├── hooks/             # Custom React hooks
│   │   └── useApi.ts
│   │
│   ├── utils/             # Utility functions
│   │   ├── formatters.ts
│   │   └── validators.ts
│   │
│   ├── App.tsx            # Main App component
│   ├── index.tsx          # Entry point
│   └── main.tsx           # Vite entry
│
├── public/                # Static assets
│   ├── index.html
│   └── favicon.svg
│
├── package.json           # NPM dependencies
├── tsconfig.json          # TypeScript configuration
├── vite.config.ts         # Vite configuration
├── tailwind.config.js     # Tailwind CSS configuration
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and npm/yarn/pnpm
- Backend API running on `http://localhost:8000`

### Installation

```bash
cd frontend
npm install
```

### Development

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Build for Production

```bash
npm run build
npm run preview  # Preview production build locally
```

## 📦 Dependencies

### Core Dependencies
- **react**: UI library
- **react-router-dom**: Client-side routing
- **typescript**: Type safety
- **axios**: HTTP client
- **zustand**: State management
- **tailwindcss**: Utility-first CSS framework

### UI & Visualization
- **plotly.js**: Interactive charts
- **react-plotly.js**: React wrapper for Plotly
- **recharts**: Additional charting library
- **lucide-react**: Icon library
- **headlessui**: Unstyled accessible components

### Form & Validation
- **react-hook-form**: Efficient form handling
- **zod**: Schema validation

### Development
- **vite**: Fast build tool
- **@vitejs/plugin-react**: React plugin for Vite
- **@typescript-eslint**: TypeScript linting
- **prettier**: Code formatter
- **vitest**: Unit testing framework

## 🔌 API Integration

The frontend communicates with the backend API:

```typescript
// Example API calls
import { api } from './services/api'

// Get DQ scorecards
const scorecards = await api.get('/validation/scorecards')

// Get quarantined records
const quarantine = await api.get('/quarantine/records')

// Get data lineage
const lineage = await api.get('/lineage/graph')
```

## 🎯 Key Pages

- **Dashboard**: Overview of all DQ metrics
- **Scorecards**: Detailed quality scores per dimension
- **Quarantine**: Manage failed records
- **Lineage**: Visualize data flow
- **Alerts**: Configure and view alerts
- **Rules**: Manage validation rules
- **Settings**: Application configuration

## 🧪 Testing

```bash
npm run test           # Run unit tests
npm run test:coverage  # Run tests with coverage
```

## 📝 Code Style

The project uses Prettier for code formatting and ESLint for linting:

```bash
npm run lint           # Run ESLint
npm run lint:fix       # Fix ESLint issues
npm run format         # Format code with Prettier
```

## 🌐 Environment Variables

Create a `.env` file in the frontend directory:

```env
VITE_API_URL=http://localhost:8000
VITE_LOG_LEVEL=info
```

## 📚 Additional Resources

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [Plotly Documentation](https://plotly.com/javascript/)

---

**Status**: Under Development | **Last Updated**: June 2026