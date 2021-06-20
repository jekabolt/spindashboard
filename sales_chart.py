import router
import plotly.express as px
import plotly.graph_objects as go
import layout
import dataframes_utils
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

    # second plot
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

    # third plot
    @router.app.callback(
        [Output(component_id='sale_calendar-3', component_property='figure'),
         Output(component_id='results-3', component_property='figure'),
         ],
        [Input(component_id='slct-year', component_property='value'),
         Input(component_id='slct-month', component_property='value')]
    )
    def update_graph_live(year, month):

        storage_df = dataframes_utils.get_current_goods_acceptance_df(
            year, month)

        plot = px.bar(storage_df,
                      x='get_day',
                      y='count',
                      color='Storage',
                      category_orders={
                          'get_day': sorted(list(storage_df['get_day']))
                      },
                      labels={'get_day': 'День',
                              'count': 'Колличество принятых товаров',
                              'Plat': 'Место хранения'}
                      )

        plot_legend = go.Figure()
        storage = set(storage_df['Storage'])
        n = len(storage)
        k = 0
        for i in storage:
            plot_legend.add_trace(
                go.Indicator(
                    mode="number",
                    value=storage_df.loc[
                        storage_df['Storage'] == i, 'count'].count(),
                    number={'prefix': i + ": ", "font": {"size": 20}},

                    domain={'x': [0, 1], 'y': [
                        k / (n + 1), (k + 1) / (n + 1)]},
                )
            )
            k += 1

        plot_legend.add_trace(
            go.Indicator(
                mode="number+delta",
                value=storage_df['count'].count(),
                number={'prefix': "Всего: ", "font": {"size": 20}},
                domain={'x': [0, 1], 'y': [n / (n + 1), 1]},))

        return plot, plot_legend

    # fourth pie

    @router.app.callback(
        [
            Output(component_id='results-4', component_property='figure'),
            Output(component_id='goods', component_property='figure')
        ],
        [
            Input(component_id='slct-year', component_property='value'),
            Input(component_id='slct-month', component_property='value')
        ]
    )
    def update_graph_live(year, month):

        storage = dataframes_utils.get_all_time_goods_acceptance_active()

        # count total amount per category
        storage_map, total_count_period = dataframes_utils.count_map(storage)

        # count percentage
        percentage_map = {}
        s = sum(storage_map.values())
        for k, v in storage_map.items():
            pct = v * 100.0 / s
            percentage_map[k] = str(format(pct, '.2f'))

        percents = list(percentage_map.values())

        goods = px.pie(
            names=[*storage_map],
            values=[*percents],
            height=600,
            width=600)

        table = go.Figure(data=[
            go.Table(
                header=dict(
                    values=['source', 'percentage', 'units in volume']),
                cells=dict(values=[[*storage_map], [*percents], [*list(storage_map.values())]]))
        ])

        return table, goods
