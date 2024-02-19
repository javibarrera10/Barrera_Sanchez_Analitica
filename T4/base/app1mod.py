# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# y luego visite el sitio
# http://127.0.0.1:8050/ 
# en su navegador.

import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas 
df = pd.DataFrame({
    "Frutas": ["Ácidas","Dulces","Ácidas","Dulces","Ácidas","Dulces"],
    "Gusto": [2, 6, 8, 10, 5, 4],
    "Edad": ["Niño", "Joven", "Adulto", "Niño", "Joven", "Adulto"]
})

fig = px.bar(df, x="Frutas", y="Gusto", color="Edad", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Frutas y gustos'),

    html.Div(children='''
        Histograma de gustos según edad y sabor
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children='''
        En este gráfico se observa el número de personas que les gustaron las frutas ácidas y dulces diferenciados por su edad
    '''),
    html.Div(
        className="Columnas",
        children=[
            html.Ul(id='my-list', children=[html.Li(i) for i in df.columns])
        ],
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
