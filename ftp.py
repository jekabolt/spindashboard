from ftplib import FTP
import datetime
import os
from dateutil import parser


def get_goods(local_goods_file_path="goods.xlsx"):
    ftp_user = os.getenv('FTP_USER')
    ftp_pass = os.environ.get('FTP_PASSWORD')
    ftp_port = os.environ.get('FTP_PORT')
    ftp_host = os.environ.get('FTP_HOST')

    ftp = FTP()
    ftp.connect(ftp_host, int(ftp_port))
    ftp.login(ftp_user, ftp_pass)
    ftp.cwd('tov')

    now = datetime.datetime.now()

    names = ftp.nlst()

    latest_time = None
    latest_name = None

    for name in names:
        time = ftp.voidcmd("MDTM " + name)
        if (latest_time is None) or (time > latest_time):
            latest_name = name
            latest_time = time

    print(latest_name)
    # ftp_file_name = now.strftime("%y_%m_%d")+".xlsx"
    # ftp_file_name = "21_04_28.xlsx"
    ftp_file_name = latest_name
    with open(local_goods_file_path, 'wb') as local_goods_file_path:
        ftp.retrbinary('retr ' + ftp_file_name, local_goods_file_path.write)
    ftp.close()
