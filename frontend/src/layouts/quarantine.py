"""
Quarantine Layout.
"""

from dash import html, dcc
import plotly.graph_objs as go

layout = html.Div([
    html.Div(
        className='quarantine-container',
        children=[
            html.H1('Quarantined Records'),
            
            html.Div(
                className='filter-section',
                children=[
                    html.Div(
                        children=[
                            html.Label('Filter by Rule:'),
                            dcc.Dropdown(
                                id='rule-filter',
                                options=[
                                    {'label': 'All Rules', 'value': 'all'},
                                    {'label': 'Null Check', 'value': 'null_check'},
                                    {'label': 'Range Check', 'value': 'range_check'},
                                ],
                                value='all'
                            )
                        ]
                    ),
                    html.Div(
                        children=[
                            html.Label('Filter by Severity:'),
                            dcc.Dropdown(
                                id='severity-filter',
                                options=[
                                    {'label': 'All Levels', 'value': 'all'},
                                    {'label': 'High', 'value': 'high'},
                                    {'label': 'Medium', 'value': 'medium'},
                                    {'label': 'Low', 'value': 'low'},
                                ],
                                value='all'
                            )
                        ]
                    )
                ]
            ),
            
            html.Div(
                className='records-table',
                children=[
                    html.Table(
                        children=[
                            html.Thead(
                                html.Tr([
                                    html.Th('Record ID'),
                                    html.Th('Source'),
                                    html.Th('Failing Rule'),
                                    html.Th('Timestamp'),
                                    html.Th('Reason'),
                                    html.Th('Action'),
                                ])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Td('REC-001'),
                                    html.Td('Source A'),
                                    html.Td('Completeness'),
                                    html.Td('2026-06-11 10:30'),
                                    html.Td('Null customer_id'),
                                    html.Td(html.Button('Resolve')),
                                ]),
                                html.Tr([
                                    html.Td('REC-002'),
                                    html.Td('Source B'),
                                    html.Td('Range Check'),
                                    html.Td('2026-06-11 10:25'),
                                    html.Td('Amount > 1000000'),
                                    html.Td(html.Button('Review')),
                                ]),
                            ])
                        ]
                    )
                ]
            ),
            
            html.Div(
                className='statistics',
                children=[
                    html.Div(
                        children=[
                            html.H3('Quarantine Statistics'),
                            dcc.Graph(
                                figure={
                                    'data': [
                                        go.Pie(
                                            labels=['Completeness', 'Accuracy', 'Consistency', 'Timeliness', 'Uniqueness'],
                                            values=[245, 128, 95, 67, 45],
                                        )
                                    ],
                                    'layout': go.Layout(title='Issues by Dimension')
                                }
                            )
                        ]
                    )
                ]
            )
        ]
    )
])