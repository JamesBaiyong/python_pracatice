# encoding=utf-8
from operator import add
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

# conf = SparkConf()
# conf.setAppName('TestDStream')
# conf.setMaster('local[2]')
sc = SparkContext('local','testDStream')
ssc = StreamingContext(sc, 4) # 设置多少秒监听一次
lines = ssc.textFileStream('file:///home/baiyong/my_code/python_pracatice/ML/spark_code/spark_streaming_file')

words = lines.flatMap(lambda line: line.split(' '))
wordCounts = words.map(lambda x : (x,1)).reduceByKey(add)
print(wordCounts.pprint())
wordCounts.pprint()

ssc.start()
ssc.awaitTermination()
