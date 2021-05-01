import dash
import dash_auth
# import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os
import layout
import dataframes
import sales_chart
from dataclasses import dataclass
import pandas


@dataclass
class Config:
    goods_filepath: str  # FILEPATH_GOODS
    ftp_user: str  # FTP_USER
    ftp_pass: str  # FTP_PASSWORD
    ftp_port: str  # FTP_PORT
    ftp_host: str  # FTP_HOST
    auth_username: str  # LOGIN_USERNAME
    auth_password: str  # LOGIN_PASSWORD


config = Config(
    goods_filepath=os.environ.get('FILEPATH_GOODS'),
    ftp_user=os.environ.get('FTP_USER'),
    ftp_pass=os.environ.get('FTP_PASSWORD'),
    ftp_port=os.environ.get('FTP_PORT'),
    ftp_host=os.environ.get('FTP_HOST'),
    auth_username=os.environ.get('LOGIN_USERNAME'),
    auth_password=os.environ.get('LOGIN_PASSWORD')
)


# init dataframes
goods_df = dataframes.start_refresh_dataframes()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# auth
VALID_USERNAME_PASSWORD_PAIRS = {
    config.auth_username: config.auth_password,
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


# init charts callbacks
sales_chart.register_sales_chart_callbacks(app)


# router
@ app.callback(Output('page-content', 'children'),
               Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/page-1":
        return layout.layout_page_1
    elif pathname == "/page-2":
        return layout.layout_page_2
    else:
        return layout.layout_index
