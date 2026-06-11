"""
Graph Components for Lineage Visualization.
"""

import plotly.graph_objs as go
import networkx as nx
from typing import Dict, List

def create_lineage_dag(nodes: List[str], edges: List[tuple]):
    """
    Create a directed acyclic graph for data lineage.
    
    Args:
        nodes: List of node names
        edges: List of edge tuples (from, to)
    
    Returns:
        Plotly figure
    """
    # Create NetworkX graph
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    # Calculate positions using hierarchical layout
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    # Extract edges for plotting
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        mode='lines',
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        showlegend=False
    )
    
    # Extract nodes for plotting
    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition='top center',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            color='#0ea5e9',
            size=20,
            line=dict(width=2, color='#fff')
        ),
        showlegend=False
    )
    
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title='Data Lineage DAG',
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='#f9fafb'
    )
    
    return fig