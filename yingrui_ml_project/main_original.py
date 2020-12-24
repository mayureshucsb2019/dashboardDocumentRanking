import dash  # (version 1.12.0) pip install dash

import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

header = html.Div([
    dbc.Row(dbc.Col(html.H1("Machine Learning Project"))),
])

query = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("QUERY", className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do",
                    className="card-value",
                )
            ]
        ),
    ],
)

document1 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(dbc.Button("DOCUMENT 1", color="link", href="https://www.google.com"), className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    className="card-value",
                )
            ]
        ),
    ],
)

document2 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(dbc.Button("DOCUMENT 2", color="link", href="https://www.google.com"), className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    className="card-value",
                )
            ]
        ),
    ],
)


analysis_header = [
    html.Thead(html.Tr([html.Th("Doc1 Score"), html.Th("Metric"), html.Th("Doc2 Score")]))
]

row1 = html.Tr([html.Td("1.1"), html.Td("Ranking-Score"), html.Td("1.2")])
row2 = html.Tr([html.Td(),html.Td(),html.Td()])
row3 = html.Tr([html.Td("1.1"), html.Td("Query-Score"), html.Td("1.2")])
row4 = html.Tr([html.Td("1.1"), html.Td("Doc-Score"), html.Td("1.2")])
row5 = html.Tr([html.Td("1.1"), html.Td("Matching"), html.Td("1.2")])
row6 = html.Tr([html.Td("1.1"), html.Td("Semantic Matching"), html.Td("1.2")])
row7 = html.Tr([html.Td("1.1"), html.Td("Syntactic Matching"), html.Td("1.2")])

analysis_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7])]

analysis = dbc.Table(
    analysis_header + analysis_body,
    bordered=True,
    dark=True,
    hover=True,
    responsive=True,
    striped=True,
)

row = dbc.Row([dbc.Col(document1, width=4), dbc.Col(analysis, width=4), dbc.Col(document2, width=4)])

#row = html.Div(
#    [
#        dbc.CardDeck(
#            [
#                document1,
#                document2
#            ]
#        ),
#    ], style={'padding': '25px'}
#)

app.layout = html.Div([
    header,
    query,
    row
])

if __name__ == "__main__":
    app.run_server(port=3000, debug=True)

