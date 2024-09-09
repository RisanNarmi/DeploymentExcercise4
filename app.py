from dash import Dash, html, dcc, callback, Input, Output # dcc is dash component
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px

app = Dash(__name__)
server = app.server

# Reading data
df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/DeploymentExcercise4/main/gdp_1960_2020.csv")

# setting figures
@callback(
    Output('graph-scatter', 'figure'),
    Output('graph-pie', 'figure'),
    Output('graph-pie2', 'figure'),
    Input('dropdown-count', 'value'),
    Input('dropdown-year', 'value'),
    Input('slider-year', 'value')
)
def update_graph(sel, yer, yerslide):
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

    subYear = df[df["year"].isin([yerslide])]
    subASIA_Year = subYear[subYear['state'].isin(['Asia'])]
    subEU_Year = subYear[subYear['state'].isin(['Europe'])]
    subOCE_Year = subYear[subYear['state'].isin(['Oceania'])]
    subAMERICAS_Year = subYear[subYear['state'].isin(['America'])]
    subAFRICA_Year = subYear[subYear['state'].isin(['Africa'])]
    chart_Lable = ["Asia", "Europe", "Oceania", "Americas", "Africa"]
    pie_data = sum(subASIA_Year["gdp"]), sum(subEU_Year["gdp"]), sum(subOCE_Year["gdp"]), sum(subAMERICAS_Year["gdp"]), sum(subAFRICA_Year["gdp"])
    pie_df = {"continent":chart_Lable,
              "gdp":pie_data}
    fig3 = px.pie(pie_df, values="gdp", names="continent")
    

    return fig, fig2, fig3

# layout set
app.layout = [html.H1('Hello, look at this graph'), 
              html.H3('Interactivity time'), 
              dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 'Malaysia', id='dropdown-count'), 
              dcc.Graph(id='graph-scatter'), 
              dcc.Dropdown([{'label':'2020', 'value':2020}, {'label':'2010', 'value':2010}, 
                            {'label':'2000', 'value':2000}], 2020, id='dropdown-year'),
              dcc.Graph(id="graph-pie")]
              dcc.Slider(1960, 2020, 5, value=2020, id='slider-year'),
              dcc.Graph(id="graph-pie2")]

if __name__ == '__main__':
    app.run(debug=True)
