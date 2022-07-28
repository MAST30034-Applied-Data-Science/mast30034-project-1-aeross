def read_parquet(filename):
    
    # This is copied from tutorial 1
    from pyspark.sql import SparkSession

    # Create a spark session (which will run spark jobs)
    spark = (
        SparkSession.builder.appName("MAST30034 Tutorial 1")
        .config("spark.sql.repl.eagerEval.enabled", True) 
        .config("spark.sql.parquet.cacheMetadata", "true")
        .getOrCreate()
    )
    return spark.read.parquet(filename)