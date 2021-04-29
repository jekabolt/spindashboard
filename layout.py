import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])


layout_page_1 = html.Div([
    dcc.Link('home', href='/'),


    html.Br(),
    html.Br(),

    # dbc.Row([
    #         dbc.Col(html.H1("data range selector", style={'text-align': 'center'}),
    #                 width={"size": 8, "offset": 2}, )]),
    #
    # dbc.Row([
    #         dbc.Col(html.A("graph 1", href="#graph-1", style={'text-align': 'center'}),
    #                 width={"size": 8, "offset": 2}, )]),
    # dbc.Row([
    #         dbc.Col(html.A("graph 2", href="#graph-2", style={'text-align': 'center'}),
    #                 width={"size": 8, "offset": 2}, )]),
    #
    # dbc.Row([
    #         dbc.Col(html.A("graph 3", href="#graph-3", style={'text-align': 'center'}),
    #                 width={"size": 8, "offset": 2}, )]),

    dcc.Dropdown(id="slct-year",
                 options=[
                     {'label': '2020', 'value': '2020'},
                     {'label': '2021', 'value': '2021'}],
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

    dbc.Row([
            dbc.Col(html.H1("total moth sales", id="graph-1", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dbc.Row([
            dbc.Col(
                [dcc.Graph(id='results', figure={})
                 ], width={"size": 3}
            ),
            dbc.Col(dcc.Graph(id='sale_calendar', figure={}), width={"size": 9})

            ]),


    # --

    dbc.Row([
            dbc.Col(html.H1("total in-kind sales 2", id="graph-2", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dbc.Row([
            dbc.Col(
                [dcc.Graph(id='results-2', figure={})
                 ], width={"size": 3}
            ),
            dbc.Col(dcc.Graph(id='sale_calendar-2',
                    figure={}), width={"size": 9})
            ]),

    # --

    dbc.Row([
            dbc.Col(html.H1("total moth sales 3", id="graph-3", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dbc.Row([
            dbc.Col(
                [dcc.Graph(id='results-3', figure={})
                 ], width={"size": 3}
            ),
            dbc.Col(dcc.Graph(id='sale_calendar-3',
                    figure={}), width={"size": 9})
            ]),

    html.Br(),
])


layout_page_2 = html.Div([
    dcc.Link('home', href='/'),

    html.Br(),
    html.Br(),

    dbc.Row([
            dbc.Col(html.H1("data range selector", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dbc.Row([
            dbc.Col(html.A("graph 1", href="#graph-1", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),
    dbc.Row([
            dbc.Col(html.A("graph 2", href="#graph-2", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dbc.Row([
            dbc.Col(html.A("graph 3", href="#graph-3", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dcc.Dropdown(id="slct-year",
                 options=[
                     {'label': '2020', 'value': '2020'},
                     {'label': '2021', 'value': '2021'}],
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

    dbc.Row([
            dbc.Col(html.H1("total moth sales", id="graph-1", style={'text-align': 'center'}),
                    width={"size": 8, "offset": 2}, )]),

    dbc.Row([
            dbc.Col(
                [dcc.Graph(id='results', figure={})
                 ], width={"size": 3}
            ),
            dbc.Col(dcc.Graph(id='sale_calendar', figure={}), width={"size": 9})

            ]),

])
