import dash
import pandas as pd
import plotly.express as px
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import openpyxl

app = dash.Dash(__name__)
server = app.server

# -------------------------------------------------------------------------------------------------------------------------
# ДАННЫЕ
# -------------------------------------------------------------------------------------------------------------------------

df = pd.read_excel('goods.xlsx', usecols="A,C:E,G,H,Z,AD,AF:AI,AN,AP", skiprows=3,
                   names=['id', 'Status', 'Date', 'Sale_Date', 'Owner', 'Rule', 'First_Price', 'Sale_Price', 'Ship',
                          'Pay_Cost', 'Plat_Cost', 'Recover', 'Plat', 'Seller'], engine='openpyxl',
                   converters={'id': str, 'Sale_Price': int})
df = df[df['Status'] == "Продажа"].drop(columns='Status')
dict_of_plats = {None: 'Grailed',
                 'VK': 'VK',
                 'Avito': 'Avito',
                 'Spin4spin': 'Grailed',
                 'TheMarket': 'VK',
                 'Лемаркет': 'VK',
                 'Ebay': 'Ebay',
                 'Spin4spin__': 'Grailed',
                 'Buyma': 'Buyma',
                 'Grailed': 'Grailed',
                 'showroom': 'Showroom',
                 'Spin4spin_': 'Grailed',
                 'Spin4spin___': 'Grailed',
                 'maahno': 'Grailed',
                 'Официальный Сайт ': 'Website',
                 'saintlaurentarchive': 'Grailed',
                 'Instagram': 'Instagram',
                 'Invoice': 'Grailed',
                 'Taobao': 'Taobao',
                 'Heroine': 'Grailed'}
df['Plat'] = df['Plat'].replace(dict_of_plats)
# df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
df['sales_month'] = df['Sale_Date'].str[3:5]
df['sales_year'] = df['Sale_Date'].str[6:]
df['sales_day'] = df['Sale_Date'].str[:2]



# -------------------------------------------------------------------------------------------------------------------------
# HTML ВЫКЛАДКА
# -------------------------------------------------------------------------------------------------------------------------

app.layout = html.Div([

    html.H1("Here is the biggest text in the world", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct-year",
                 options=[
                     {'label': '2020', 'value': '2020'},
                     {'label': '2021', 'value': '2021'} ],
                 multi=False,
                 value='2021',
                 style={'width': '40%'}
                 ),
    dcc.Dropdown(id="slct-month",
                 options=[
                     {'label': 'Январь', 'value': '01'},
                     {'label': 'Февраль', 'value': '02'},
                     {'label': 'Март', 'value': '03'},
                     {'label': 'Апрель', 'value': '04'},
                     {'label': 'Май', 'value': '05'},
                     {'label': 'Июнь', 'value': '06'},
                     {'label': 'Июль', 'value': '07'},
                     {'label': 'Август', 'value': '08'},
                     {'label': 'Сентябрь', 'value': '09'},
                     {'label': 'Октябрь', 'value': '10'},
                     {'label': 'Ноябрь', 'value': '11'},
                     {'label': 'Декабрь', 'value': '12'}
                 ],
                 multi=False,
                 value='03',
                 style={'width': '40%'}
                 ),

    html.Br(),

    dcc.Graph(id='sale_calendar', figure={}),
    html.Br(),
])


# --------------------------------------------------
# Наполнение элементов СМЫСЛОМ

@app.callback(
    Output(component_id='sale_calendar', component_property='figure'),
    [Input(component_id='slct-year', component_property='value'),
     Input(component_id='slct-month', component_property='value')]
)
def update_graph(year, month):

    dff = df.copy()

    dff = dff[(dff['sales_year'] == year) & (dff['sales_month'] == month)]

    day_order = sorted(list(dff['sales_day']))
    # plotly
    fig = px.bar(dff, x='sales_day', y='Sale_Price', color='Plat', category_orders={'sales_day': day_order}
                 , template="plotly_dark")
    #
    # fig = px.choropleth(

    #     data_frame=dff,
    #     locationmode='USA-states',
    #     locations='state_code',
    #     scope="usa",
    #     color='Pct of Colonies Impacted',
    #     hover_data=['State', 'Pct of Colonies Impacted'],
    #     color_continuous_scale=px.colors.sequential.YlOrRd,
    #     labels={'Pct of Colonies Impacted': '% of bee colonies'},
    #     template='plotly_dark'

    return fig


# запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)
