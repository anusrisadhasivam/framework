"""
Data Lineage Layout.
"""

from dash import html, dcc
import plotly.graph_objs as go

layout = html.Div([
    html.Div(
        className='lineage-container',
        children=[
            html.H1('Data Lineage'),
            
            html.Div(
                className='lineage-controls',
                children=[
                    html.Button('Expand All', id='expand-btn'),
                    html.Button('Collapse All', id='collapse-btn'),
                    html.Button('Export', id='export-btn'),
                ]
            ),
            
            html.Div(
                className='lineage-graph',
                children=[
                    html.H3('Data Flow DAG'),
                    dcc.Graph(
                        figure={
                            'data': [
                                go.Scatter(
                                    x=[0, 1, 2, 3],
                                    y=[3, 2, 1, 0],
                                    mode='markers+text',
                                    text=['Source A', 'Validation', 'Quarantine', 'Analytics'],
                                    textposition='top center',
                                    marker=dict(
                                        size=30,
                                        color=['#0ea5e9', '#10b981', '#f59e0b', '#8b5cf6']
                                    )
                                ),
                            ],
                            'layout': go.Layout(
                                title='Data Flow Lineage',
                                xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                                hovermode='closest',
                            )
                        }
                    )
                ]
            ),
            
            html.Div(
                className='lineage-details',
                children=[
                    html.H3('Node Details'),
                    html.Table(
                        children=[
                            html.Thead(
                                html.Tr([
                                    html.Th('Node'),
                                    html.Th('Type'),
                                    html.Th('Records Processed'),
                                    html.Th('Records Failed'),
                                ])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Td('Source A'),
                                    html.Td('Ingestion'),
                                    html.Td('1.2M'),
                                    html.Td('-'),
                                ]),
                                html.Tr([
                                    html.Td('Validation'),
                                    html.Td('Processing'),
                                    html.Td('1.2M'),
                                    html.Td('156K'),
                                ]),
                                html.Tr([
                                    html.Td('Analytics'),
                                    html.Td('Consumption'),
                                    html.Td('1.04M'),
                                    html.Td('-'),
                                ]),
                            ])
                        ]
                    )
                ]
            )
        ]
    )
])