import dash
import pandas as pd
import plotly.express as px
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

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

current_month = '03'
current_year = '2021'
month_of_sales = df[(df['sales_month'] == current_month) & (df['sales_year'] == current_year)]
day_order = sorted(list(month_of_sales['sales_day']))

total_sales = month_of_sales['Sale_Price'].sum()

# -------------------------------------------------------------------------------------------------------------------------
# HTML ВЫКЛАДКА
# -------------------------------------------------------------------------------------------------------------------------

app.layout = html.Div([

    html.H1("Here is the biggest text in the world", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct-month",
                 options=[
                     {'label': '2020', 'value': '2020'},
                     {'label': '2021', 'value': '2021'}, ],
                 multi=False,
                 value=2015,
                 style={'width': '40%'}
                 ),
    dcc.Dropdown(id="slct-month",
                 options=[
                     {'label': 'Январь', 'value': 2015},
                     {'label': 'Февраль', 'value': 2016},
                     {'label': 'Март', 'value': 2017},
                     {'label': 'Апрель', 'value': 2018},
                     {'label': 'Май', 'value': 2015},
                     {'label': 'Июнь', 'value': 2016},
                     {'label': 'Июль', 'value': 2017},
                     {'label': 'Август', 'value': 2018},
                     {'label': 'Сентябрь', 'value': 2015},
                     {'label': 'Октябрь', 'value': 2016},
                     {'label': 'Ноябрь', 'value': 2017},
                     {'label': 'Декабрь', 'value': 2018}
                 ],
                 multi=False,
                 value=2015,
                 style={'width': '40%'}
                 ),

    html.Br(),

    dcc.Graph(id='sale_calendar', figure={}),
    html.Br(),
])


# --------------------------------------------------
# Наполнение элементов СМЫСЛОМ

@app.callback(
    [Output(component_id='sale_calendar', component_property='figure')],
    [Input(component_id='slct-year', component_property='value'),
     Input(component_id='slct-month', component_property='value')]
)
def update_graph(month, year):

    dff = df.copy()
    dff = dff[(dff['sales_year'] == year) & (dff['sales_month'] == month)]

    # plotly
    fig = px.bar(month_of_sales, x='sales_day', y='Sale_Price', color='Plat', category_orders={'sales_day': day_order}
                 , template="plotly_dark")
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
