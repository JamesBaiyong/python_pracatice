# encoding=utf-8
import sys
from pyspark import SparkContext
reload(sys)
sys.setdefaultencoding('utf8')

"""
使用spark读取s3指定目录文件
spark-submit --jars ./sparks_jar/aws-java-sdk-1.7.4.jar,hadoop-aws-2.7.3.jar spark_read_s3.py
"""


class SparkDownloadS3Files(object):
    #  s3环境
    AWS_ACCESS_KEY_ID = 'ID'
    AWS_SECRET_ACCESS_KEY = 'KEY'
    AWS_REGION_NAME = 'AWS_REGION_NAME'

    sc = SparkContext('local', 'test')
    # s3环境
    sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", AWS_ACCESS_KEY_ID)
    sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
    sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.cn-north-1.amazonaws.com.cn")

    def load_file(self):
        # 读取文件
        # self.s3_data = sc.textFile("s3a://test/text1/2018/10/31/*.t*xt")
        self.s3_data = self.sc.wholeTextFiles("s3a://text/text1/2018/10/31/")

        print(self.s3_data.collect())
        # 简单存起来做验证
        for i in self.s3_data.collect():
            print('key', i[0])
            print(i[1])
            name = i[0].split('/')
            with open('%s' % str(name[-1]), 'w') as f:
                f.write(i[1])

    def run_task(self):
        self.load_file()
        print('ok......')


if __name__ == '__main__':
    De = SparkDownloadS3Files()
    De.run_task()
