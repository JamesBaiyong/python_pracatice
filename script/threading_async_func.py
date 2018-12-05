# coding:utf-8
import time
import threading


def test(value):
    print('start test \n')
    time.sleep(3)
    print('input %s' % value)

if __name__ == '__main__':
    t = threading.Thread(target=test, args=(u'hello async',))
    t.start()
    print('start hello async 2')