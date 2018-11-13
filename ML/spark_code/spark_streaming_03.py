# encoding=utf-8
import time

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="test_python_streaming_queue_stream")
    ssc = StreamingContext(sc, 1)


    rddQueue = []
    for i in range(4):
        rddQueue += [ssc.sparkContext.parallelize([j for j in range(1, 4)], 10)]


    inputStream = ssc.queueStream(rddQueue)
    mappedStream = inputStream.map(lambda x: (x * 10, 1))
    reducedStream = mappedStream.reduceByKey(lambda a, b: a + b)
    reducedStream.pprint()

    ssc.start()
    time.sleep(4)
    ssc.stop(stopSparkContext=True, stopGraceFully=True) # 关闭程序