import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("data/sostenibilidad_mensual.csv")

app = dash.Dash(__name__)
app.title = "Dashboard de Sostenibilidad"

app.layout = html.Div([
    html.H1("Dashboard de Sostenibilidad 2024", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id="unidad-dropdown",
        options=[{"label": u, "value": u} for u in df["Unidad"].unique()],
        value="Unidad 1"
    ),

    dcc.Graph(id="grafico-energia"),
    dcc.Graph(id="grafico-co2"),
    dcc.Graph(id="grafico-reciclaje")
])

@app.callback(
    dash.dependencies.Output("grafico-energia", "figure"),
    dash.dependencies.Input("unidad-dropdown", "value")
)
def update_energia(unidad):
    dff = df[df["Unidad"] == unidad]
    fig = px.line(dff, x="Mes", y="Energia_kWh", title="Consumo de Energía (kWh)")
    return fig

@app.callback(
    dash.dependencies.Output("grafico-co2", "figure"),
    dash.dependencies.Input("unidad-dropdown", "value")
)
def update_co2(unidad):
    dff = df[df["Unidad"] == unidad]
    fig = px.line(dff, x="Mes", y="CO2_kg", title="Emisiones de CO₂ (kg)")
    return fig

@app.callback(
    dash.dependencies.Output("grafico-reciclaje", "figure"),
    dash.dependencies.Input("unidad-dropdown", "value")
)
def update_reciclaje(unidad):
    dff = df[df["Unidad"] == unidad]
    fig = px.bar(dff, x="Mes", y="Reciclaje_%", title="Porcentaje de Residuos Reciclados")
    return fig

if __name__ == "__main__":
    app.run_server(debug=False)
