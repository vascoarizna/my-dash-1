# Import necessary libraries 

import dash_bootstrap_components as dbc
import seaborn as sns
import plotly.express as px
from dash import dcc
from dash import html


diamonds = sns.load_dataset("diamonds")

scatter = px.scatter(
   data_frame=diamonds,
   x="price",
   y="carat",
   color="cut",
   title="Carat vs. Price of Diamonds",
   width=600,
   height=400,
)
histogram = px.histogram(
   data_frame=diamonds,
   x="price",
   title="Histogram of Diamond prices",
   width=600,
   height=400,
)
violin = px.violin(
   data_frame=diamonds,
   x="cut",
   y="price",
   title="Violin Plot of Cut vs. Price",
   width=600,
   height=400,
)

left_fig = html.Div(children=dcc.Graph(figure=scatter))
right_fig = html.Div(children=dcc.Graph(figure=histogram))






upper_div = html.Div([left_fig, right_fig], style={"display": "flex"})
central_div = html.Div(
   children=dcc.Graph(figure=violin),
   style={"display": "flex", "justify-content": "center"},
)


# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Page 4 - Multiplot")),
        html.Br(),
        html.Div([upper_div, central_div])
    ])
])


