import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

// Placeholder components - to be implemented
const Dashboard = () => <div className="p-8"><h1 className="text-3xl font-bold">Dashboard</h1></div>
const Scorecards = () => <div className="p-8"><h1 className="text-3xl font-bold">Scorecards</h1></div>
const Quarantine = () => <div className="p-8"><h1 className="text-3xl font-bold">Quarantine</h1></div>
const Lineage = () => <div className="p-8"><h1 className="text-3xl font-bold">Lineage</h1></div>
const Alerts = () => <div className="p-8"><h1 className="text-3xl font-bold">Alerts</h1></div>
const Rules = () => <div className="p-8"><h1 className="text-3xl font-bold">Rules</h1></div>
const Settings = () => <div className="p-8"><h1 className="text-3xl font-bold">Settings</h1></div>

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <h1 className="text-xl font-bold text-primary-600">DQ Framework</h1>
              </div>
              <div className="flex items-center space-x-4">
                <a href="/" className="text-gray-600 hover:text-gray-900">Dashboard</a>
                <a href="/scorecards" className="text-gray-600 hover:text-gray-900">Scorecards</a>
                <a href="/quarantine" className="text-gray-600 hover:text-gray-900">Quarantine</a>
                <a href="/lineage" className="text-gray-600 hover:text-gray-900">Lineage</a>
                <a href="/alerts" className="text-gray-600 hover:text-gray-900">Alerts</a>
                <a href="/rules" className="text-gray-600 hover:text-gray-900">Rules</a>
                <a href="/settings" className="text-gray-600 hover:text-gray-900">Settings</a>
              </div>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/scorecards" element={<Scorecards />} />
          <Route path="/quarantine" element={<Quarantine />} />
          <Route path="/lineage" element={<Lineage />} />
          <Route path="/alerts" element={<Alerts />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App