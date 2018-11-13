# encoding=utf-8
from pyspark import SparkContext
# hello wold 级别的spark应用,统计文本中的词率

sc = SparkContext('local', 'test')
file = "./test_data/hello_world.md"
all_file = sc.textFile(file)

wordCount = all_file.flatMap(lambda line: line.split(' '))\
    .map(lambda word:(word,1))\
    .reduceByKey(lambda a,b:a + b)

collect_list = wordCount.collect()
for i in collect_list:
    print(i)
