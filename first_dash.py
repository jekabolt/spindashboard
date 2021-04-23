import dash
import dash_auth
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import openpyxl
import os
import layout
import goods

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# auth
VALID_USERNAME_PASSWORD_PAIRS = {
    os.environ.get('LOGIN_USERNAME'): os.environ.get('LOGIN_PASSWORD'),
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# layout
app.layout = layout.url_bar_and_content_div

app.validation_layout = html.Div([
    layout.url_bar_and_content_div,
    layout.layout_index,
    layout.layout_page_1,
    layout.layout_page_2,
])

df = goods.get_goods_df()


# --------------------------------------------------
# Наполнение элементов СМЫСЛОМ
#


@app.callback(
    [Output(component_id='sale_calendar', component_property='figure'),
     Output(component_id='results', component_property='figure'),
     ],
    [Input(component_id='slct-year', component_property='value'),
     Input(component_id='slct-month', component_property='value')]
)
def update_graph_live(year, month):
    dff = df.copy()
    print(month, year)
    dff = dff[(dff['sales_year'] == year) & (dff['sales_month'] == month)]

    day_order = sorted(list(dff['sales_day']))
    calendar = px.bar(dff, x='sales_day', y='Sale_Price', color='Plat', category_orders={'sales_day': day_order},
                      labels={'sales_day': 'День',
                              'Sale_Price': 'Цена продажи', 'Plat': 'Площадка'}
                      )

    results = go.Figure()
    wheres = set(dff['Plat'])
    n = len(wheres)
    k = 0
    for i in wheres:
        results.add_trace(
            go.Indicator(
                mode="number+delta",
                value=dff.loc[dff['Plat'] == i, 'Sale_Price'].sum(),
                number={'prefix': i + ": ", "font": {"size": 20}},
                # delta={'reference': 8000000},
                domain={'x': [0, 1], 'y': [k / (n + 1), (k + 1) / (n + 1)]},

            )
        )
        k += 1
    results.add_trace(
        go.Indicator(
            mode="number+delta",
            value=dff['Sale_Price'].sum(),
            number={'prefix': "Всего: ", "font": {"size": 20}},
            # delta={'position': "top", 'reference': 8000000},
            domain={'x': [0, 1], 'y': [n / (n + 1), 1]},))

    return calendar, results


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/page-1":
        return layout.layout_page_1
    elif pathname == "/page-2":
        return layout.layout_page_2
    else:
        return layout.layout_index


if __name__ == '__main__':
    app.run_server(debug=True)
