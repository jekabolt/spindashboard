import dash
import pandas as pd
import plotly.express as px
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv("intro_bees.csv")
df = df.groupby(['State','ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

app.layout = html.Div([

    html.H1("Here is the biggest text in the world", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct-year",
        options=[
            {'label': '2015', 'value': 2015},
            {'label': '2016', 'value': 2016},
            {'label': '2017', 'value': 2017},
            {'label': '2018', 'value': 2018}],
        multi=False,
        value=2015,
        style={'width': '40%'}
    ),

    html.Div(id="output_container", children=[]),
    html.Br(),

    dcc.Graph(id = 'my_bee_map', figure={}),
    html.Br(),
])

# --------------------------------------------------
# Наполнение элементов СМЫСЛОМ

@app.callback(
    [Output(component_id="output_container", component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
     [Input(component_id='slct-year', component_property='value')])
def update_graph(option):
    print(option)
    print(type(option))

    container = "The year chosen: {}".format(option)
    dff = df.copy()
    dff = dff[dff["Year"] == option]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    # plotly
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope = "usa",
        color= 'Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of bee colonies'},
        template='plotly_dark'
    )
    return container, fig

# запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)