# encoding=utf-8
from pyspark import SparkContext

sc = SparkContext('local', 'test')

# 并行集合创建RDD
test_lines = ['python', 'scala', 'java', 'python', 'golang', 'spark']
rdd = sc.parallelize(test_lines)
# 创建pairRDD,key为列表中的元素,value为1
pairRdd = rdd.map((lambda key: (key, 1)))

# 常用的键值对转换操作


def test_keys():
    # reduceByKey(func)的功能是, 使用func函数合并具有相同键的值
    reduce_key = pairRdd.reduceByKey(lambda a, b: a + b)
    print('合并具有相同建的值')
    print(reduce_key.collect())

    # groupByKey()的功能是,对具有相同键的值进行分组
    group_by_key = pairRdd.groupByKey()
    print('对具有相同建的值分组')
    print(group_by_key.collect())

    # keys()只会把键值对RDD中的key返回形成一个新的RDD
    keys = pairRdd.keys()
    print('只取key')
    print(keys.collect())

    # values()只会把键值对RDD中的value返回形成一个新的RDD
    values = pairRdd.values()
    print('只取value')
    print(values.collect())

    # sortByKey()的功能是返回一个根据键排序的RDD
    sort_by_key = pairRdd.sortByKey()
    print('按照键排序')
    print(sort_by_key.collect())

    # 对键值对RDD的value部分进行处理,而不是同时对key和value进行处理
    map_value = pairRdd.mapValues(lambda a: a + 1)
    print('对value做操作')
    print(map_value.collect())

    # join表示内连接,连接两个pairRdd中想同的key,合并value,如同关系型数据库中的内链接
    pair_rdd1 = sc.parallelize([('python', 'hadoop')])
    join = pairRdd.join(pair_rdd1)
    print('内连接两个不同的简直对RDD')
    print(join.collect())


def test_all_op():
    # 计算每个键的平均数
    test_rdd = sc.parallelize(
        [("spark", 2), ("hadoop", 6), ("hadoop", 4), ("spark", 6), ("python", 22)])
    res = test_rdd.mapValues(lambda x: (x, 1))
    res1 = res.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    avg_res = res1.mapValues(lambda x: (x[0] / x[1]))
    print('求每个键的平均数的三步操作')
    print(res.collect())
    print(res1.collect())
    print(avg_res.collect())


test_keys()
test_all_op()

"""
out:
合并具有相同建的值
[('python', 2), ('golang', 1), ('spark', 1), ('java', 1), ('scala', 1)]
对具有相同建的值分组
[('python', <pyspark.resultiterable.ResultIterable object at 0x7f2f0ee085d0>),
 ('golang', <pyspark.resultiterable.ResultIterable object at 0x7f2f0ee08c10>),
 ('spark', <pyspark.resultiterable.ResultIterable object at 0x7f2f0ee08c50>),
 ('java', <pyspark.resultiterable.ResultIterable object at 0x7f2f0ee08c90>),
 ('scala', <pyspark.resultiterable.ResultIterable object at 0x7f2f0ee08cd0>)]
只取key
['python', 'scala', 'java', 'python', 'golang', 'spark']
只取value
[1, 1, 1, 1, 1, 1]
按照键排序
[('golang', 1), ('java', 1), ('python', 1), ('python', 1), ('scala', 1), ('spark', 1)]
对value做操作
[('python', 2), ('scala', 2), ('java', 2), ('python', 2), ('golang', 2), ('spark', 2)]
内连接两个不同的简直对RDD
[('python', (1, 'hadoop')), ('python', (1, 'hadoop'))]
求每个键的平均数的三步操作
[('spark', (2, 1)), ('hadoop', (6, 1)), ('hadoop', (4, 1)), ('spark', (6, 1)), ('python', (22, 1))]
[('python', (22, 1)), ('spark', (8, 2)), ('hadoop', (10, 2))]
[('python', 22), ('spark', 4), ('hadoop', 5)]
"""
