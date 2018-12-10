# encoding=utf-8
from pyspark.sql import SparkSession, SQLContext
import hashlib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def gen_hash_id(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10):
    # 组合字段生成hash id
    lists = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    strs = ''
    for i_str in lists:
        try:
            if i_str:
                i_str_tmp = i_str.encode("utf-8")
                item = str(i_str_tmp).replace('null', '').replace('None', '')
            else:
                item = ''
        except BaseException:
            item = ''
            print(type(i_str))
        strs += item
    print(strs)
    hash_id = hashlib.md5(strs).hexdigest()
    return hash_id


sc = SparkSession.builder\
    .appName('test') \
    .getOrCreate()

scc = sc.sparkContext
file = "./test_data/nh_gh_com.csv"
df01 = sc.read.load(file, format='csv', delimiter=',', header=True)
df01.createOrReplaceTempView("nh_table")


df02 = sc.sql(
    "select address,death_date,enterprise_name,enterprise_status,enterprise_type,"
    "legal_person,history_name,open_to,operate_scope,reg_cap "
    " from nh_table")
df02.createOrReplaceTempView('t2')
df02.show(10)

# 注册函数
sqlContext = SQLContext(sparkContext=scc)
sqlContext.registerFunction("gen_hash_id", gen_hash_id)
df03 = sc.sql('select enterprise_name,'
              ' gen_hash_id(address,death_date,enterprise_name,'
              'enterprise_status,enterprise_type,legal_person,'
              'history_name,open_to,operate_scope,'
              'reg_cap) as hash_id '
              'from t2')
df03.createOrReplaceTempView('t3')

res = sc.sql('select t3.hash_id, t1.* '
             'from nh_table t1, t3'
             ' where t1.enterprise_name = t3.enterprise_name')
res.repartition(1).write.save(
    './test.csv',
    format="csv",
    header=False,
    delimiter=',',
    mode="overwrite")
