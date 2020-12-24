import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

from app import app
from components.navbar import nav_bar
from utils import util

header = html.Div([
    dbc.Row(dbc.Col(html.H1("Machine Learning Project"))),
])

queryText = "California Santa Barabra beach side"

doc1 = "California, officially the State of California, is a state in the Pacific Region of the United States of America. With over 39.5 million residents across a total area of about 163,696 square miles (423,970 km2), California is the most populous U.S. state and the third-largest by area, and is also the world's thirty-fourth most populous subnational entity. California is also the most populated subnational entity in North America, and has its state capital in Sacramento. The Greater Los Angeles area and the San Francisco Bay Area are the nation's second- and fifth-most populous urban regions, with 18.7 million and 9.7 million residents respectively.[14] Los Angeles is California's most populous city, and the country's second-most populous, after New York City. California also has the nation's most populous county, Los Angeles County, and its largest county by area, San Bernardino County. The City and County of San Francisco is both the country's second most densely populated major city after New York City and the fifth most densely populated county, behind only four of the five New York City boroughs."

doc2 = "Santa Barbara (Spanish: Santa Bárbara; Spanish for 'Saint Barbara') is a coastal city in, and the county seat of, Santa Barbara County in the U.S. state of California. Situated on a south-facing section of coastline, the longest such section on the West Coast of the United States, the city lies between the steeply rising Santa Ynez Mountains and the Pacific Ocean. Santa Barbara's climate is often described as Mediterranean, and the city has been promoted as the American Riviera.[11] As of 2019, the city had an estimated population of 91,364,[12] up from 88,410 in 2010, making it the second most populous city in the county after Santa Maria.[13] The contiguous urban area, which includes the cities of Goleta and Carpinteria, along with the unincorporated regions of Isla Vista, Montecito, Mission Canyon, Hope Ranch, Summerland, and others, has an approximate population of 220,000. The population of the entire county in 2010 was 423,895.[14] "

metric = {"California":1, "Santa":2, "Barabra":3, "beach":4, "side":5}

colorMaper = util.colorMaper(metric)

metric1_score_doc1 = {}
metric2_score_doc2 = {}

colorText1 = []
colorText2 = []
colorQueryText = []

histogram1 = util.generateFrequency(doc1)
histogram2 = util.generateFrequency(doc2)

df1 = pd.DataFrame({"tokens":histogram1[0], "freq":histogram1[1]})
fig1 = px.histogram(df1, x="tokens", y="freq")
fig1.update_layout(barmode="stack",xaxis={"categoryorder":"total descending"})

df2 = pd.DataFrame({"tokens":histogram2[0], "freq":histogram2[1]})
fig2 = px.histogram(df2, x="tokens", y="freq")
fig2.update_layout(barmode="stack",xaxis={"categoryorder":"total descending"})

query = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("QUERY", className="card-title"),
                html.P(
                    colorQueryText if colorQueryText !=[] else queryText,
                    id = "id-query",
                    className="card-value",
                )
            ]
        ),
    ],
)

dropdown = dcc.Dropdown(id="my-id", 
                        options=[
                                 {"label": "Ranking-Score", "value": "1"},
                                 {"label": "Query-Score", "value": "2"},
                                 {"label": "Doc-Score", "value": "3"},
                                 {"label": "Matching", "value": "4"},                        
                                 {"label": "Semantic-Matching", "value": "5"},
                                 {"label": "Syntactic-Matching", "value": "6"}
                        ],
                        value="Initial Text"
                       )

 	  	
document1 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(dbc.Button("DOCUMENT 1", color="link", href="./app2"), className="card-title"),
                html.P(
                    colorText1 if colorText1 != [] else doc1,
                    id="id-doc1",
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
                html.H4(dbc.Button("DOCUMENT 2", color="link", href="./app2"), className="card-title"),
                html.P(
                    colorText2 if colorText2 != [] else doc2,
                    id="id-doc2",
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
row2 = html.Br()
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

layout = html.Div([
    nav_bar,
    header,
    query,
    dropdown,
    html.Br(),
    row,
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('id-query', 'children'),
    Input('my-id', 'value'))
def display_value(value):
    global queryText
    if(value == "1"):
        colorQueryText = util.makeTokens(queryText, metric, colorMaper)
        return colorQueryText
    return queryText

@app.callback(
    Output('id-doc1', 'children'),
    Input('my-id', 'value'))
def display_value(value):
    global colorText1, doc1
    if(value == "1"):
        colorText1 = util.makeTokens(doc1, metric, colorMaper)
        return colorText1
    return doc1

@app.callback(
    Output('id-doc2', 'children'),
    Input('my-id', 'value'))
def display_value(value):
    global colorText2,doc2
    if(value == "1"):
        colorText2 = util.makeTokens(doc2, metric, colorMaper)
        return colorText2
    return doc2
