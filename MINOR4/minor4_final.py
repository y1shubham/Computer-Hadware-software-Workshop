# -*- coding: utf-8 -*-
"""MINOR4_FINAL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p6bykhpcXR2eKFDXSvmrqKuytPlm5Iij
"""

!pip install pyspark

# from google.colab import drive
# drive.mount('/content/drive')

# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, sum
# import pandas as pd
# import os

# spark = SparkSession.builder \
#     .appName("SalesDataAnalysis") \
#     .getOrCreate()

# sales_data = spark.read.csv("Sales_data.csv", header=True, inferSchema=True)
# sales_data.show()
# sales_data = sales_data.dropDuplicates()
# sales_data = sales_data.na.drop()
# sales_data.show()
# sales_data = sales_data.groupBy("Product").agg(sum("Amount").alias("TotalSales"))
# sales_data.write.csv("result.csv", header=True)
# csv_files = [file for file in os.listdir("result.csv") if file.endswith('.csv')]
# result_df = pd.concat([pd.read_csv(os.path.join("result.csv", file)) for file in csv_files])
# print(result_df)
# spark.stop()



sales_data = sales_data.dropDuplicates()

sales_data = sales_data.na.drop()



sales_data = sales_data.na.drop()

sales_data = sales_data.dropDuplicates()

sales_data.show()

sales_data = sales_data.groupBy("Product").agg(sum("Amount").alias("TotalSales"))

sales_data.write.csv("result.csv", header=True)

csv_files = [file for file in os.listdir("result.csv") if file.endswith('.csv')]
result_df = pd.concat([pd.read_csv(os.path.join("result.csv", file)) for file in csv_files])
print(result_df)

spark.stop()

pip install jupyter nbconvert

jupyter nbconvert --to script MINOR4_FINAL.ipynb