# Import necessary libraries 
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from dash import html, dcc, callback, Input, Output

df = px.data.stocks()


# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Page 5 - DropDown")),
        html.Br(),
        dcc.Dropdown(id='dropdown',
                     options=[
                         {'label': 'Google', 'value': 'GOOG'},
                         {'label': 'Apple', 'value': 'AAPL'},
                         {'label': 'Amazon', 'value': 'AMZN'},
                     ],
                     value='GOOG'),
        dcc.Graph(id='bar_plot')
    ])
])




@callback(Output(component_id='bar_plot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])

def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x=df['date'], y=df['{}'.format(dropdown_value)], \
                                line=dict(color='firebrick', width=4))
                     ])

    fig.update_layout(title='Stock prices over time',
                      xaxis_title='Dates',
                      yaxis_title='Prices'
                      )
    return fig
