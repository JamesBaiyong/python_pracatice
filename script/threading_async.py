# encoding=utf-8
import threading
import time

class TestAsync(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    # 继承Thread需要重写run方法, 线程在开启后运行
    def run(self):
        print('start test\n')
        time.sleep(3)  # 休息3秒,模拟等待
        print('input %s' % self.value)

if __name__ == '__main__':
    worker = TestAsync('hello async')
    worker.start()
    print('async do func start..')