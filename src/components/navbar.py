# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("HOME", href="/home")),
                dbc.NavItem(dbc.NavLink("1-Page 1", href="/page1")),
                dbc.NavItem(dbc.NavLink("2-Small Table w/ columns", href="/page2")),
                dbc.NavItem(dbc.NavLink("3-SimplePlot", href="/page3")),
                dbc.NavItem(dbc.NavLink("4-Multiplot", href="/page4")),
                dbc.NavItem(dbc.NavLink("5-Stocks with Dropdown", href="/page5")),
            ] ,
            brand="Dashboard - Testing",
            brand_href="/home",
            color="dark",
            dark=True,
        ), 
    ])

    return layout
