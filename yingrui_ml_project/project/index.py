import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from components import navbar
from apps import app1, app2


header = html.Div([
    dbc.Row(dbc.Col(html.H1("Machine Learning Project"))),
])

index_layout = html.Div([
    navbar.nav_bar,
    header,
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.P(),
    dcc.Link('Go to App 2', href='/apps/app2')
])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return index_layout
    elif pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return 'Page not found: 404'

if __name__ == '__main__':
    app.run_server(port=3000, debug=True)
