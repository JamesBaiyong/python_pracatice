# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 19-2-27 上午11:59
# @author: scdev030
import time
from multiprocessing.dummy import Pool as ThreadPool
import requests

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.pythsadffsdfsdgdfsgon.org/community/awardsafdsafsdfasdfds/'
    ]

def get_url_content(url):
    """
    请求网页
    """
    try:
        return requests.get(url, timeout=20)
    except:
        return url

# 创建进程池
pool = ThreadPool(4)

# 在各自进程打开url,　并且返回函数中的返回结果
start_time = time.time()
results = pool.map(get_url_content, urls)

#　关闭进程池, 等待进程完成
pool.close()
pool.join()
end_time = time.time()

print('pool 4 spend : %s'%(end_time-start_time))
for i in results:
    print(i)
