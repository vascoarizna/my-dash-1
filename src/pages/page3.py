# Import necessary libraries 
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px


# Load dataset using Plotly
tips = px.data.tips()

fig = px.scatter(tips, x="total_bill", y="tip") # Create a scatterplot


# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Page 3")),
        html.Br(),
        html.Center(html.H3('This is a small example')),
        html.Br(),
        html.Hr(),
        dcc.Graph(
               id='example-graph',
               figure=fig
           )

    ])
])