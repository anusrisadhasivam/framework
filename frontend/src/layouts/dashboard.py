"""
Main Dashboard Layout.
"""

from dash import html, dcc
import plotly.graph_objs as go
from datetime import datetime, timedelta

# Dashboard layout
layout = html.Div([
    html.Div(
        className='dashboard-container',
        children=[
            html.H1('Data Quality Dashboard'),
            
            # KPI Cards
            html.Div(
                className='kpi-cards',
                children=[
                    html.Div(className='kpi-card', children=[
                        html.H3('Overall Quality Score'),
                        html.Div(className='kpi-value', children='85.4%')
                    ]),
                    html.Div(className='kpi-card', children=[
                        html.H3('Records Validated'),
                        html.Div(className='kpi-value', children='1.2M')
                    ]),
                    html.Div(className='kpi-card', children=[
                        html.H3('Failed Records'),
                        html.Div(className='kpi-value', children='156K')
                    ]),
                    html.Div(className='kpi-card', children=[
                        html.H3('Active Alerts'),
                        html.Div(className='kpi-value', children='12')
                    ]),
                ]
            ),
            
            # Charts
            html.Div(
                className='charts-row',
                children=[
                    html.Div(
                        className='chart',
                        children=[
                            html.H3('Quality Trend (7 Days)'),
                            dcc.Graph(
                                figure={
                                    'data': [
                                        go.Scatter(
                                            x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                                            y=[85, 84, 85.5, 86, 84.5, 86.5, 85.4],
                                            mode='lines+markers',
                                            name='Quality Score'
                                        )
                                    ],
                                    'layout': go.Layout(
                                        title='Quality Score Trend',
                                        xaxis_title='Day',
                                        yaxis_title='Quality Score (%)',
                                        hovermode='x unified'
                                    )
                                }
                            )
                        ]
                    ),
                    html.Div(
                        className='chart',
                        children=[
                            html.H3('Quality by Dimension'),
                            dcc.Graph(
                                figure={
                                    'data': [
                                        go.Bar(
                                            x=['Completeness', 'Accuracy', 'Consistency', 'Timeliness', 'Uniqueness'],
                                            y=[92, 88, 82, 85, 80],
                                            marker_color=['#0ea5e9', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
                                        )
                                    ],
                                    'layout': go.Layout(
                                        title='Quality Scores by Dimension',
                                        xaxis_title='Dimension',
                                        yaxis_title='Score (%)',
                                        hovermode='x unified'
                                    )
                                }
                            )
                        ]
                    ),
                ]
            ),
            
            # Recent Issues
            html.Div(
                className='recent-issues',
                children=[
                    html.H3('Recent Issues'),
                    html.Table(
                        children=[
                            html.Thead(
                                html.Tr([
                                    html.Th('Source'),
                                    html.Th('Issue'),
                                    html.Th('Count'),
                                    html.Th('Severity'),
                                ])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Td('Source A'),
                                    html.Td('Null values'),
                                    html.Td('245'),
                                    html.Td(html.Span('High', className='severity-high')),
                                ]),
                                html.Tr([
                                    html.Td('Source B'),
                                    html.Td('Duplicates'),
                                    html.Td('128'),
                                    html.Td(html.Span('Medium', className='severity-medium')),
                                ]),
                            ])
                        ]
                    )
                ]
            )
        ]
    )
])