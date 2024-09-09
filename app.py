from dash import Dash, html, dcc
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px

app = Dash(__name__)
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/DeploymentTestMCM7183Ex3/main/gdp_1960_2020.csv")

subMY = df[df["country"].isin(["Malaysia"])]
sub2020 = df[df["year"].isin([2020])]
subASIA_2020 = sub2020[sub2020['state'].isin(['Asia'])]
subEU_2020 = sub2020[sub2020['state'].isin(['Europe'])]
subOCE_2020 = sub2020[sub2020['state'].isin(['Oceania'])]
subAMERICAS_2020 = sub2020[sub2020['state'].isin(['America'])]
subAFRICA_2020 = sub2020[sub2020['state'].isin(['Africa'])]
chart_Lable = ["Asia", "Europe", "Oceania", "Americas", "Africa"]
pie_data = sum(subASIA_2020["gdp"]), sum(subEU_2020["gdp"]), sum(subOCE_2020["gdp"]), sum(subAMERICAS_2020["gdp"]), sum(subAFRICA_2020["gdp"])
pie_df = {"continent":chart_Lable,
         "gdp":pie_data}

fig = px.scatter(subMY, x="year", y="gdp")
fig2 = px.pie(pie_df, values="gdp", names="continent")

app.layout = [html.H1('Hello, look at this graph'), dcc.Graph(figure=fig), dcc.Graph(figure=fig2)]

if __name__ == '__main__':
    app.run(debug=True)
