from dash import Dash, html, dcc, callback, Input, Output # dcc is dash component
import numpy as np 
import pandas as pd 
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
app.title = "MCM7183 Exercise 3"
server = app.server

# Reading data
df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/ImranNasir_242PM243TP_DeploymentExcercise3/refs/heads/main/gdp_1960_2020.csv")

# setting figures
@callback(
    Output('graph-scatter', 'figure'),
    Output('graph-pie', 'figure'),
    Input('dropdown-count', 'value'),
    Input('dropdown-year', 'value'),
)
def update_graph(sel, yer):
    subCountry = df[df["country"].isin([sel])]
    fig = px.scatter(subCountry, x="year", y="gdp")

    subYear = df[df["year"].isin([yer])]
    subASIA_Year = subYear[subYear['state'].isin(['Asia'])]
    subEU_Year = subYear[subYear['state'].isin(['Europe'])]
    subOCE_Year = subYear[subYear['state'].isin(['Oceania'])]
    subAMERICAS_Year = subYear[subYear['state'].isin(['America'])]
    subAFRICA_Year = subYear[subYear['state'].isin(['Africa'])]
    chart_Lable = ["Asia", "Europe", "Oceania", "Americas", "Africa"]
    pie_data = sum(subASIA_Year["gdp"]), sum(subEU_Year["gdp"]), sum(subOCE_Year["gdp"]), sum(subAMERICAS_Year["gdp"]), sum(subAFRICA_Year["gdp"])
    pie_df = {"continent":chart_Lable,
              "gdp":pie_data}
    fig2 = px.pie(pie_df, values="gdp", names="continent")

    return fig, fig2

# layout set
app.layout = [html.H1('Hello, look at this graph'), 
              html.H3('Interactivity time'), 
              dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 'Malaysia', id='dropdown-country'),
              dcc.Graph(id="graph-scatter"), 
              #dcc.Dropdown([{'label':'2020', 'value':2020}, {'label':'2010', 'value':2010}, 
              #              {'label':'2000', 'value':2000}], 2020, id='dropdown-year'),
              dcc.Slider(1960, 2020, 5, value=2020, id='slider-year',
                         marks = {i: str(i) for i in range(1960, 2021, 5)}),
              dcc.Graph(id="graph-pie")]

if __name__ == '__main__':
    app.run(debug=True)
