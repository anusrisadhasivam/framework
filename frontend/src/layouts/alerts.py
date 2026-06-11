"""
Alerts Layout.
"""

from dash import html, dcc
import plotly.graph_objs as go

layout = html.Div([
    html.Div(
        className='alerts-container',
        children=[
            html.H1('Data Quality Alerts'),
            
            html.Div(
                className='alert-stats',
                children=[
                    html.Div(className='stat-card', children=[
                        html.H3('Active Alerts'),
                        html.Div(className='stat-value', children='12')
                    ]),
                    html.Div(className='stat-card', children=[
                        html.H3('Critical'),
                        html.Div(className='stat-value critical', children='3')
                    ]),
                    html.Div(className='stat-card', children=[
                        html.H3('Warning'),
                        html.Div(className='stat-value warning', children='9')
                    ]),
                ]
            ),
            
            html.Div(
                className='alerts-list',
                children=[
                    html.H3('Active Alerts'),
                    html.Table(
                        children=[
                            html.Thead(
                                html.Tr([
                                    html.Th('Alert ID'),
                                    html.Th('Metric'),
                                    html.Th('Current Value'),
                                    html.Th('Threshold'),
                                    html.Th('Severity'),
                                    html.Th('Triggered At'),
                                ])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Td('ALR-001'),
                                    html.Td('Completeness'),
                                    html.Td('78%'),
                                    html.Td('80%'),
                                    html.Td(html.Span('Critical', className='severity-critical')),
                                    html.Td('2026-06-11 15:30'),
                                ]),
                                html.Tr([
                                    html.Td('ALR-002'),
                                    html.Td('Accuracy'),
                                    html.Td('82%'),
                                    html.Td('85%'),
                                    html.Td(html.Span('Warning', className='severity-warning')),
                                    html.Td('2026-06-11 14:15'),
                                ]),
                            ])
                        ]
                    )
                ]
            ),
            
            html.Div(
                className='alert-history',
                children=[
                    html.H3('Alert History'),
                    dcc.Graph(
                        figure={
                            'data': [
                                go.Bar(
                                    x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                                    y=[2, 3, 1, 4, 2, 1, 3],
                                    name='Alerts Triggered',
                                    marker_color='#ef4444'
                                )
                            ],
                            'layout': go.Layout(
                                title='Daily Alert Frequency',
                                xaxis_title='Day',
                                yaxis_title='Number of Alerts',
                            )
                        }
                    )
                ]
            )
        ]
    )
])