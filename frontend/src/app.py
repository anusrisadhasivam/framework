"""
Main Dash Application for Data Quality Dashboard.
"""

import os
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
from dotenv import load_dotenv

from src.layouts import dashboard, scorecards, quarantine, lineage, alerts
from src.services.api_client import APIClient

# Load environment variables
load_dotenv()

# Initialize API Client
api_url = os.getenv('BACKEND_API_URL', 'http://localhost:8000')
api_client = APIClient(api_url)

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Data Quality Validation Framework"

# Define app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Navigation bar
navbar = html.Nav(
    className='navbar',
    children=[
        html.Div(
            className='navbar-container',
            children=[
                html.H1('Data Quality Framework', className='navbar-title'),
                html.Ul(
                    className='navbar-menu',
                    children=[
                        html.Li(html.A('Dashboard', href='/dashboard')),
                        html.Li(html.A('Scorecards', href='/scorecards')),
                        html.Li(html.A('Quarantine', href='/quarantine')),
                        html.Li(html.A('Lineage', href='/lineage')),
                        html.Li(html.A('Alerts', href='/alerts')),
                    ]
                )
            ]
        )
    ]
)

# Page routing callback
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """Route to appropriate page based on URL."""
    if pathname == '/scorecards':
        return html.Div([navbar, scorecards.layout])
    elif pathname == '/quarantine':
        return html.Div([navbar, quarantine.layout])
    elif pathname == '/lineage':
        return html.Div([navbar, lineage.layout])
    elif pathname == '/alerts':
        return html.Div([navbar, alerts.layout])
    else:
        return html.Div([navbar, dashboard.layout])


if __name__ == '__main__':
    debug_mode = os.getenv('DASH_DEBUG', 'True').lower() == 'true'
    app.run_server(debug=debug_mode, host='0.0.0.0', port=8050)