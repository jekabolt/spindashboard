import os
import ftp
import pandas as pd

# meh
def get_goods_df():
    goods_fp = os.environ.get('FILEPATH_GOODS')
    if not os.path.isfile(goods_fp):
        # not exist
        ftp.get_goods(goods_fp)

    df = pd.read_excel(goods_fp, usecols="A,C:E,G,H,Z,AD,AE,AF:AI,AN,AP,AX,AY", skiprows=3,
                       names=['id', 'Status', 'Date', 'Sale_Date', 'Owner', 'Rule', 'First_Price', 'Sale_Price','Vypl', 'Ship',
                              'Pay_Cost', 'Plat_Cost', 'Recover', 'Plat', 'Seller','Vypl_Counted','Storage'], engine='openpyxl',
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
    # df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
    df['sales_month'] = df['Sale_Date'].str[3:5]
    df['sales_year'] = df['Sale_Date'].str[6:]
    df['sales_day'] = df['Sale_Date'].str[:2]
    df['get_month'] = df['Date'].str[3:5]
    df['get_year'] = df['Date'].str[6:]
    df['get_day'] = df['Date'].str[:2]

    df['count'] = 1
    df = df.drop_duplicates(subset=['id'])
    return df
