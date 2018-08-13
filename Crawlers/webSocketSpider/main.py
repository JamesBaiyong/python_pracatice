import websocket
import thread
import time
import pprint
import json
from config.loggingSet import SetLog
log = SetLog()
logger = log.create_logger()
headers={
    'Accept-Encoding:gzip, deflate, sdch','Accept-Language:zh-CN,zh;q=0.8',
         'Cache-Control:no-cache','Host:120.27.195.4:9502',
         'Origin:http://viewapi.kxt.com','Pragma:no-cache',
         'Sec-WebSocket-Extensions:permessage-deflate; client_max_window_bits',
         'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    }
url = 'ws://118.31.236.175:9502/?token=sHdy2IF5eqh9daXYf4Goypl6z6eTh3xpgYuF2oK1dpaxd3aTgXiwmop4ndWLkKHWfp3SnJp8hWOXe6DGf5Ks2cegnc2YZ3-okYSZ05eBhtaOZZyngp2qnJekhteVlIfPu2V3zI59gpp_mq3Zf42C1oR3yqiIiJaogYuB2nzPZaA'


def on_message(ws, message):
    print('get')
    # pprint.pprint(message)
    mess = eval(message)
    logger.info( json.dumps(mess,indent=4,ensure_ascii=False))

def on_error(ws, error):
    print(2)
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        while True:
            ws.send('{"cmd":"login","number":100,"codes":["CJRL","KUAIXUN"]}')
            time.sleep(60)
        # ws.close()

    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        url,on_message = on_message,
        on_error = on_error,
        on_close = on_close,
        header=headers)
    ws.on_open = on_open
    ws.run_forever()
