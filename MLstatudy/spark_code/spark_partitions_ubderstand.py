# encoding=utf-8
from pyspark import SparkContext
import time

nums = range(0, 10)
print(nums)

def get_expend_time(f):
    print('+' * 100)
    start = time.time()
    def wrapper(*args, **kwargs):
        f()
        end = time.time()
        print('Spend time of: %s' % (end - start))
        print('+'*100)
    return wrapper()

#RDD
@get_expend_time
def test_1():
    with SparkContext("local") as sc:
        rdd = sc.parallelize(nums)
        print("Default parallelism: {}".format(sc.defaultParallelism))
        print("Number of partitions: {}".format(rdd.getNumPartitions()))
        print("Partitioner: {}".format(rdd.partitioner))
        print("Partitions structure: {}".format(rdd.glom().collect()))

@get_expend_time
def test_2():
    with SparkContext("local") as sc:
        rdd = sc.parallelize(nums).repartition(3)
        print("Default parallelism: {}".format(sc.defaultParallelism))
        print("Number of partitions: {}".format(rdd.getNumPartitions()))
        print("Partitioner: {}".format(rdd.partitioner))
        print("Partitions structure: {}".format(rdd.glom().collect()))

@get_expend_time
def test_3():
    with SparkContext("local") as sc:
        rdd = sc.parallelize(nums).repartition(15)
        print("Number of partitions: {}".format(rdd.getNumPartitions()))
        print("Partitioner: {}".format(rdd.partitioner))
        print("Partitions structure: {}".format(rdd.glom().collect()))

#pairRDD
@get_expend_time
def test_4():
    with SparkContext("local[2]") as sc:
        rdd = sc.parallelize(nums) \
            .map(lambda el: (el, el)) \
            .partitionBy(3) \
            .persist()

        print("Number of partitions: {}".format(rdd.getNumPartitions()))
        print("Partitioner: {}".format(rdd.partitioner))
        print("Partitions structure: {}".format(rdd.glom().collect()))


from pyspark.rdd import portable_hash
num_partitions = 2
for el in nums:
    print("Element: [{}]: {} % {} = partition {}".format(
        el, portable_hash(el), num_partitions, portable_hash(el) % num_partitions))
#
@get_expend_time
def test_6():
    transactions = [
        {'name': 'Bob', 'amount': 100, 'country': 'United Kingdom'},
        {'name': 'James', 'amount': 15, 'country': 'United Kingdom'},
        {'name': 'Marek', 'amount': 51, 'country': 'Poland'},
        {'name': 'Johannes', 'amount': 200, 'country': 'Germany'},
        {'name': 'Paul', 'amount': 75, 'country': 'Poland'},
    ]

    def country_partitioner(country):
        return hash(country)
    # Validate results
    num_partitions = 5
    print(country_partitioner("Poland") % num_partitions)
    print(country_partitioner("Germany") % num_partitions)
    print(country_partitioner("United Kingdom") % num_partitions)

    with SparkContext("local[2]") as sc:
        rdd = sc.parallelize(transactions) \
            .map(lambda el: (el['country'], el)) \
            .partitionBy(3, country_partitioner)

        print("Number of partitions: {}".format(rdd.getNumPartitions()))
        print("Partitioner: {}".format(rdd.partitioner))
        print("Partitions structure: {}".format(rdd.glom().collect()))

@get_expend_time
def test_7():
    transactions = [
        {'name': 'Bob', 'amount': 100, 'country': 'United Kingdom'},
        {'name': 'James', 'amount': 15, 'country': 'United Kingdom'},
        {'name': 'Marek', 'amount': 51, 'country': 'Poland'},
        {'name': 'Johannes', 'amount': 200, 'country': 'Germany'},
        {'name': 'Paul', 'amount': 75, 'country': 'Poland'},
    ]
    def country_partitioner(country):
        return hash(country)

    def sum_sales(iterator):
        yield sum(transaction[1]['amount'] for transaction in iterator)

    with SparkContext("local[2]") as sc:
        by_country = sc.parallelize(transactions) \
            .map(lambda el: (el['country'], el)) \
            .partitionBy(3, country_partitioner)

        print("Partitions structure: {}".format(by_country.glom().collect()))

        # Sum sales in each partition
        sum_amounts = by_country \
            .mapPartitions(sum_sales) \
            .collect()

        print("Total sales for each partition: {}".format(sum_amounts))