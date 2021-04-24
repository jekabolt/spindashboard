import server
import plotly.express as px
import plotly.graph_objects as go
import layout
from dash.dependencies import Input, Output


def register_sales_chart_callbacks(app):
    # first plot
    @server.app.callback(
        [Output(component_id='sale_calendar', component_property='figure'),
         Output(component_id='results', component_property='figure'),
         ],
        [Input(component_id='slct-year', component_property='value'),
         Input(component_id='slct-month', component_property='value')]
    )
    def update_graph_live(year, month):
        df = server.goods_df.copy()
        print(month, year)
        df = df[(df['sales_year'] == year) & (df['sales_month'] == month)]

        day_order = sorted(list(df['sales_day']))
        calendar = px.bar(df, x='sales_day', y='Sale_Price', color='Plat', category_orders={'sales_day': day_order},
                          labels={'sales_day': 'День',
                                  'Sale_Price': 'Цена продажи', 'Plat': 'Площадка'}
                          )

        results = go.Figure()
        wheres = set(df['Plat'])
        n = len(wheres)
        k = 0
        for i in wheres:
            results.add_trace(
                go.Indicator(
                    mode="number+delta",
                    value=df.loc[df['Plat'] == i, 'Sale_Price'].sum(),
                    number={'prefix': i + ": ", "font": {"size": 20}},
                    # delta={'reference': 8000000},
                    domain={'x': [0, 1], 'y': [
                        k / (n + 1), (k + 1) / (n + 1)]},

                )
            )
            k += 1
        results.add_trace(
            go.Indicator(
                mode="number+delta",
                value=df['Sale_Price'].sum(),
                number={'prefix': "Всего: ", "font": {"size": 20}},
                # delta={'position': "top", 'reference': 8000000},
                domain={'x': [0, 1], 'y': [n / (n + 1), 1]},))

        return calendar, results
