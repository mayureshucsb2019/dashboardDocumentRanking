import os
os.path.abspath

import dash_bootstrap_components as dbc


nav_bar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
    ],
    brand="UCSB-PROJECT",
    brand_href="#",
    color="primary",
    dark=True,
)
