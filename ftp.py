from ftplib import FTP
import datetime
import os
from dateutil import parser
import router
import schedule
import time


def get_goods(local_goods_file_path="goods.xlsx"):
    ftp = FTP()
    ftp.connect(router.config.ftp_host, int(router.config.ftp_port))
    ftp.login(router.config.ftp_user, router.config.ftp_pass)
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

    print("get_goods latest filename", latest_name)
    # latest_name = now.strftime("%y_%m_%d")+".xlsx"
    # ftp_file_name = "21_04_28.xlsx"
    with open(local_goods_file_path, 'wb') as local_goods_file_path:
        ftp.retrbinary('retr ' + latest_name, local_goods_file_path.write)
    ftp.close()
