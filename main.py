import server
import ftp
import os

if __name__ == '__main__':
    goods_fp = os.environ.get('FILEPATH_GOODS')
    ftp.get_goods(goods_fp)
    server.app.run_server(debug=True)
