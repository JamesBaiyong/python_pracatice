# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 19-3-15 上午11:51
# @author: scdev030
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(
    hosts='xx.xx.xx.xx',
    port='9200'
)
# 过滤,查早发布时间晚于2019-03-14 00:00:00,指定字段的文本
body = {
    "query": {
        "bool": {
            "filter": {
                "range": {
                    "published_time": {
                        "gte": "2019-03-14 00:00:00"
                    }
                }
            }
        }
    },
    "_source": [
        "id",
        "published_time",
        "title"
    ]
}

index = "your_es_index"
doc_type = "your_es_doc_type"


def search_by_default():
    """
    按照时间筛选,默认返回10条
    """
    search_result = es.search(body=body, index=index, doc_type=doc_type)
    print(type(search_result))
    print(json.dumps(search_result))


def search_by_scroll():
    """
    使用可翻页的方式查询
    """
    scroll_search_result = es.search(body=body, index=index, doc_type=doc_type, scroll='1m')
    page = scroll_search_result['hits'].get('total', 0)
    scroll_id = scroll_search_result.get('_scroll_id')

    while page > 0:
        print(page)
        print(scroll_id)
        # print(json.dumps(scroll_search_result, indent=4, ensure_ascii=False))
        scroll_search_result = es.scroll(scroll_id=scroll_id, scroll='2m')
        page = len(scroll_search_result['hits'].get('hits'))
        scroll_id = scroll_search_result.get('_scroll_id')

search_by_scroll()
