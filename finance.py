# подгружаем необходимые библиотеки
import dash
import pandas as pd
import plotly.express as px

# ------------------------------------------------------------------------------------------------------------
# получаем данные о продажах
df = pd.read_excel('goods.xlsx', usecols="A,C:E,G,H,Z,AD,AF:AI,AN,AP", skiprows=3,
                   names=['id', 'Status', 'Date', 'Sale_Date', 'Owner', 'Rule', 'First_Price', 'Sale_Price', 'Ship',
                          'Pay_Cost', 'Plat_Cost', 'Recover', 'Plat', 'Seller'], engine='openpyxl',
                   converters={'id': str, 'Sale_Price': int})
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
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
df['month'] = df['Date'].str[3:5]
df['year'] = df['Date'].str[6:]
df['day'] = df['Date'].str[:2]
current_month = '03'
current_year = '2021'
month_of_sales = df[(df['month'] == current_month) & (df['year'] == current_year)]
print(month_of_sales.shape)
# month_of_sales = month_of_sales.sort_values('sales_day')
# day_order = sorted(list(month_of_sales['sales_day']))
#
# total_sales = month_of_sales['Sale_Price'].sum()
# fig = px.bar(month_of_sales, x='sales_day', y='Sale_Price', color='Plat', category_orders={'sales_day': day_order}
#              , template="plotly_dark")
#
# fig.show()
# # # # ------------------------------------------------------------------------------------------------------------
# #
# # app = dash.Dash(__name__)
# # server = app.server
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# ------------------------------------------------------------------------------------------------------------
#
# theme = {
#     'dark': True,
#     'detail': '#007439',
#     'primary': '#00EA64',
#     'secondary': '#6E6E6E',
# }
# # ------------------------------------------------------------------------------------------------------------
#
# app.layout = html.Div([
#
#     dbc.Row([
#         dbc.Col(html.H1("Finance Dataframe", style={'text-align': 'center'}),
#                 width={"size": 8, "offset": 2}, )
#
#     ]),
#
#     dbc.Row(
#         [
#             dbc.Col(daq.Gauge(
#                 id='my-gauge',
#                 label="Default",
#                 value=6,
#                 min=0,
#                 max=20,
#                 color=theme['primary']
#
#             ), width=2),
#             dbc.Col(daq.Gauge(
#                 id='my-gauge1',
#                 label="Default",
#                 value=6,
#                 min=0,
#                 max=20,
#                 color=theme['primary']
#
#             ), width=2),
#         ]),
#
#     dbc.Row(
#         [
#             dbc.Col(daq.Gauge(
#                 id='my-gauge2',
#                 label="Default",
#                 value=6,
#                 min=0,
#                 max=20,
#                 color=theme['primary']
#
#             ), width=2),
#             dbc.Col(daq.Gauge(
#                 id='my-gauge3',
#                 label="Default",
#                 value=6,
#                 min=0,
#                 max=20,
#                 color=theme['primary']
#
#             ), width=2),
#         ]),
#
#     dcc.Slider(
#         id='my-gauge-slider',
#         min=0,
#         max=10,
#         step=1,
#         value=5
#     ),
# ])
#
#
# # ------------------------------------------------------------------------------------------------------------
#
# @app.callback(
#     dash.dependencies.Output('my-gauge', 'value'),
#     [dash.dependencies.Input('my-gauge-slider', 'value')]
# )
# def update_output(value):
#     return value
#
#
# # ------------------------------------------------------------------------------------------------------------
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
