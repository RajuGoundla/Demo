import os


from snowflake.snowpark.session import Session
from snowflake.snowpark import functions as F 
from snowflake.snowpark.types import StructType,StructField,StringType,IntegerType,FloatType

from snowflake.snowpark.types import *
import pandas as pd

from snowflake.snowpark.functions import udf

from snowflake.snowpark.functions import col


# connection parameter
connection_parameters = {

"ACCOUNT":"iv45230.ap-south-1.aws",
"USER":"Raju",
"PASSWORD":"7036217979@rR",
"ROLE":"ACCOUNTADMIN",
"warehouse":"compute_wh",
"DATABASE":"demo",
"SCHEMA":"demo1",}


# creating a session
session = Session.builder.configs(connection_parameters).create()

#session.sql("use warehouse compute_wh").collect()

#a = session.table("ss").filter(col("A") >= 90)

#b = a.select(col("A","B")).collect()

print("Current data base : ",session.get_current_schema())


# a = StructType([StructField("a1",StringType()),
#                 StructField("b1",StringType())])

# #b = session.read.schema(a).option({"field_delimiter", ",","skip_header": 1 }).csv("@inter/data_0_0_0.csv.gz")

# b = session.read.schema(a).option("field_delimiter", ",").option("skip_header", 1).csv("@inter/data_0_0_0.csv.gz")


# c = b.order_by(col("a1"))
# #b = session.read.schema(a).option({"delimiter":","}).csv("@inter/data_0_0_0.csv.gz")

# c = c.collect()

# for d in c: print(d)



#a = session.table("snowflake_sample_data.tpch_sf1.customer")

#b = a.filter(col("c_mktsegment") == 'household')

#c = a.select(col("c_name"),col("c_address"))







