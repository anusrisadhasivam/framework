"""
Table Components.
"""

from dash import html

def create_data_table(columns, rows):
    """
    Create a data table.
    
    Args:
        columns: List of column names
        rows: List of row data (dictionaries)
    
    Returns:
        HTML table
    """
    return html.Table(
        children=[
            html.Thead(
                html.Tr([html.Th(col) for col in columns])
            ),
            html.Tbody([
                html.Tr([html.Td(row.get(col, '')) for col in columns])
                for row in rows
            ])
        ],
        className='data-table'
    )