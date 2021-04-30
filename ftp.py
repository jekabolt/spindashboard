from ftplib import FTP
import datetime
import os


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

    # ftp_file_name = now.strftime("%y_%m_%d")+".xlsx"
    ftp_file_name = "21_04_28.xlsx"
    with open(local_goods_file_path, 'wb') as local_goods_file_path:
        ftp.retrbinary('retr ' + ftp_file_name, local_goods_file_path.write)
    ftp.close()
