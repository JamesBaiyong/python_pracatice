from pyspark.sql import SparkSession, Row

with SparkSession.builder \
        .master("local[2]") \
        .config("spark.sql.shuffle.partitions", 50) \
        .getOrCreate() as spark:
    transactions = [
        {'name': 'Bob', 'amount': 100, 'country': 'United Kingdom'},
        {'name': 'James', 'amount': 15, 'country': 'United Kingdom'},
        {'name': 'Marek', 'amount': 51, 'country': 'Poland'},
        {'name': 'Johannes', 'amount': 200, 'country': 'Germany'},
        {'name': 'Paul', 'amount': 75, 'country': 'Poland'},
    ]
    rdd = spark.sparkContext \
        .parallelize(transactions) \
        .map(lambda x: Row(**x))

    df = spark.createDataFrame(rdd)

    print("Number of partitions: {}".format(df.rdd.getNumPartitions()))
    print("Partitioner: {}".format(rdd.partitioner))
    print("Partitions structure: {}".format(df.rdd.glom().collect()))

    # Repartition by column
    df2 = df.repartition("country")

    print("\nAfter 'repartition()'")
    print("Number of partitions: {}".format(df2.rdd.getNumPartitions()))
    print("Partitioner: {}".format(df2.rdd.partitioner))
    print("Partitions structure: {}".format(df2.rdd.glom().collect()))