# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc



# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("MAIN PAGE")),
        html.Br(),
        html.Hr(),
        html.Center([
            html.P("<center>HELLO!</center>"),
#            html.P("Welcome "+username)
        ])
    ])
])
