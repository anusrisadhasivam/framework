"""
Scorecard Layout.
"""

from dash import html, dcc
import plotly.graph_objs as go

layout = html.Div([
    html.Div(
        className='scorecards-container',
        children=[
            html.H1('Data Quality Scorecards'),
            
            html.Div(
                className='filter-section',
                children=[
                    html.Label('Select Source:'),
                    dcc.Dropdown(
                        id='source-selector',
                        options=[
                            {'label': 'All Sources', 'value': 'all'},
                            {'label': 'Source A', 'value': 'source_a'},
                            {'label': 'Source B', 'value': 'source_b'},
                        ],
                        value='all'
                    )
                ]
            ),
            
            html.Div(
                className='scorecard-grid',
                children=[
                    html.Div(
                        className='scorecard',
                        children=[
                            html.H3('Completeness'),
                            html.Div(className='score', children='92%'),
                            html.P('All required fields populated'),
                        ]
                    ),
                    html.Div(
                        className='scorecard',
                        children=[
                            html.H3('Accuracy'),
                            html.Div(className='score', children='88%'),
                            html.P('Data correctly represents reality'),
                        ]
                    ),
                    html.Div(
                        className='scorecard',
                        children=[
                            html.H3('Consistency'),
                            html.Div(className='score', children='82%'),
                            html.P('Data uniform across sources'),
                        ]
                    ),
                    html.Div(
                        className='scorecard',
                        children=[
                            html.H3('Timeliness'),
                            html.Div(className='score', children='85%'),
                            html.P('Data is current'),
                        ]
                    ),
                    html.Div(
                        className='scorecard',
                        children=[
                            html.H3('Uniqueness'),
                            html.Div(className='score', children='80%'),
                            html.P('No duplicate records'),
                        ]
                    ),
                ]
            ),
            
            html.Div(
                className='chart',
                children=[
                    html.H3('Historical Scores'),
                    dcc.Graph(
                        figure={
                            'data': [
                                go.Scatter(x=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
                                          y=[85, 84, 85.5, 86, 85.4],
                                          name='Overall Score'),
                            ],
                            'layout': go.Layout(
                                title='Quality Score Trend',
                                xaxis_title='Date',
                                yaxis_title='Score (%)'
                            )
                        }
                    )
                ]
            )
        ]
    )
])