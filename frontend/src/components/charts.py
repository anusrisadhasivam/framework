"""
Chart Components.
"""

import plotly.graph_objs as go

def create_time_series_chart(data, title):
    """
    Create a time series chart.
    
    Args:
        data: Dictionary with 'x' and 'y' keys
        title: Chart title
    
    Returns:
        Plotly figure
    """
    return go.Figure(
        data=[go.Scatter(x=data['x'], y=data['y'], mode='lines+markers')],
        layout=go.Layout(title=title, hovermode='x unified')
    )

def create_bar_chart(data, title):
    """
    Create a bar chart.
    
    Args:
        data: Dictionary with 'x' and 'y' keys
        title: Chart title
    
    Returns:
        Plotly figure
    """
    return go.Figure(
        data=[go.Bar(x=data['x'], y=data['y'])],
        layout=go.Layout(title=title, xaxis_title='Category', yaxis_title='Value')
    )

def create_gauge_chart(value, title, threshold=80):
    """
    Create a gauge chart.
    
    Args:
        value: Current value
        title: Chart title
        threshold: Alert threshold
    
    Returns:
        Plotly figure
    """
    return go.Figure(
        data=[go.Indicator(
            mode='gauge+number+delta',
            value=value,
            title=title,
            domain={'x': [0, 1], 'y': [0, 1]},
            delta={'reference': threshold},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': 'darkblue'},
                   'steps': [
                       {'range': [0, threshold-10], 'color': 'lightgray'},
                       {'range': [threshold-10, threshold], 'color': 'yellow'},
                       {'range': [threshold, 100], 'color': 'lightgreen'}
                   ]}
        )]
    )