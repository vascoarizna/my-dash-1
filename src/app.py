# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output
# Connect to your app pages
from pages import index,page1, page2,page3,page4,page5
# Connect the navbar to the index
from components import navbar
import dash
import dash_bootstrap_components as dbc
import dash_auth
from users import USERNAME_PASSWORD_PAIRS
import dash
import dash_auth
#import dash_html_components as html
from dash.dependencies import Input, Output
from flask import request



app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)

server = app.server

# Keep this out of source code repository - save in a file or a database
#VALID_USERNAME_PASSWORD_PAIRS = {"hello": "world"}
VALID_USERNAME_PASSWORD_PAIRS = USERNAME_PASSWORD_PAIRS
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)



# define the navbar
nav = navbar.Navbar()
#Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    if pathname == '/page3':
        return page3.layout

    if pathname == '/page4':
        return page4.layout
    if pathname == '/page5':
        return page5.layout


    if pathname == '/':
        return index.layout
    if pathname == '/home':
        return index.layout
    else:
        return "404 Page Error! Please choose a link"

# app.layout = html.Div([
#     html.H2(id='show-output', children='')
# ], className='container')
#
# @app.callback(
#     Output(component_id='show-output', component_property='children')
# )
# def update_output_div(n_clicks):
#     username = request.authorization['username']
#     if n_clicks:
#         return username
#     else:
#         return ''


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
