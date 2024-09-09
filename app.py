from dash import Dash, html, dcc, callback, Input, Output # dcc is dash component
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px

app = Dash(__name__)
server = app.server

# Reading data
df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/DeploymentExcercise4/main/gdp_1960_2020.csv")

# layout set
app.layout = [html.H1('Hello, look at this graph'), 
              html.H3('Interactivity time'), 
              dcc.Dropdown(['Malaysia, Indonesia, China'], 'Malaysia', id='dropdown-count'), 
              dcc.Graph(id='graph-scatter'), 
              dcc.Graph(figure=fig2)]

# Setting Paramaters
subYear = df[df["year"].isin([2020])]
subASIA_Year = sub2020[sub2020['state'].isin(['Asia'])]
subEU_Year = sub2020[sub2020['state'].isin(['Europe'])]
subOCE_Year = sub2020[sub2020['state'].isin(['Oceania'])]
subAMERICAS_Year = sub2020[sub2020['state'].isin(['America'])]
subAFRICA_Year = sub2020[sub2020['state'].isin(['Africa'])]
chart_Lable = ["Asia", "Europe", "Oceania", "Americas", "Africa"]
pie_data = sum(subASIA_Year["gdp"]), sum(subEU_Year["gdp"]), sum(subOCE_Year["gdp"]), sum(subAMERICAS_Year["gdp"]), sum(subAFRICA_Year["gdp"])
pie_df = {"continent":chart_Lable,
         "gdp":pie_data}

# setting figures
fig2 = px.pie(pie_df, values="gdp", names="continent")

@callback(
    Output('graph-scatter', 'figure'),
    Input('dropdown-count', 'value')
)
def update_graph(sel):
    subCountry = df[df["country"].isin(["sel"])]
    fig = px.scatter(subCountry, x="year", y="gdp")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
