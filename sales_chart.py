import router
import plotly.express as px
import plotly.graph_objects as go
import layout
from dash.dependencies import Input, Output


def register_sales_chart_callbacks(app):
    # first plot
    @router.app.callback(
        [Output(component_id='sale_calendar', component_property='figure'),
         Output(component_id='results', component_property='figure'),
         ],
        [Input(component_id='slct-year', component_property='value'),
         Input(component_id='slct-month', component_property='value')]
    )
    def update_graph_live(year, month):
        df = router.goods_df.copy()
        df = df.drop_duplicates()
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

    @router.app.callback(
        [Output(component_id='sale_calendar-2', component_property='figure'),
         Output(component_id='results-2', component_property='figure'),
         ],
        [Input(component_id='slct-year', component_property='value'),
         Input(component_id='slct-month', component_property='value')]
    )
    def update_graph_live(year, month):
        df = router.goods_df.copy()
        df = df.drop_duplicates(subset=['id'])
        df = df[(df['sales_year'] == year) & (df['sales_month'] == month)]

        day_order = sorted(list(df['sales_day']))
        calendar = px.bar(df, x='sales_day', y='count', color='Plat', category_orders={'sales_day': day_order},
                          labels={'sales_day': 'День',
                                  'Sale_Price': 'Колличество продаж', 'Plat': 'Площадка'}
                          )

        results = go.Figure()
        wheres = set(df['Plat'])
        n = len(wheres)
        k = 0
        for i in wheres:

            results.add_trace(
                go.Indicator(
                    mode="number+delta",
                    value=df.loc[df['Plat'] == i, 'Sale_Price'].count(),
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
                value=df['Sale_Price'].count(),
                number={'prefix': "Всего: ", "font": {"size": 20}},
                # delta={'position': "top", 'reference': 8000000},
                domain={'x': [0, 1], 'y': [n / (n + 1), 1]},))

        return calendar, results

    @router.app.callback(
        [Output(component_id='sale_calendar-3', component_property='figure'),
         Output(component_id='results-3', component_property='figure'),
         Output(component_id='goods', component_property='figure')
         ],
        [Input(component_id='slct-year', component_property='value'),
         Input(component_id='slct-month', component_property='value')]
    )
    def update_graph_live(year, month):
        df = router.goods_df.copy()
        df['Storage'] = df.Storage.fillna('Не указано')
        df1 = df.copy()
        df1 = df1[df1['Status'] == 'Приемка']

        df = df[(df['get_year'] == year) & (df['get_month'] == month)]
        active = df.copy()

        active = active[active['Status'] == 'Приемка']
        # print(active)
        # TODO:
        active['Storage'] = active.Storage.fillna('Не указано')
        day_order = sorted(list(active['get_day']))
        calendar = px.bar(active, x='get_day', y='count', color='Storage', category_orders={'get_day': day_order},
                          labels={'get_day': 'День',
                                  'count': 'Колличество принятых товаров', 'Plat': 'Место хранения'}
                          )

        results = go.Figure()
        wheres = set(active['Storage'])
        n = len(wheres)
        k = 0
        for i in wheres:
            results.add_trace(
                go.Indicator(
                    mode="number",
                    value=active.loc[active['Storage'] == i, 'count'].count(),
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
                value=active['count'].count(),
                number={'prefix': "Всего: ", "font": {"size": 20}},
                # delta={'position': "top", 'reference': 8000000},
                domain={'x': [0, 1], 'y': [n / (n + 1), 1]},))

        goods = px.pie(df1,
                       names='Storage',
                       values='count',
                       height=800,
                       width=800)

        return calendar, results, goods
