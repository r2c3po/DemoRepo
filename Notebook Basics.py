# Databricks notebook source
print("hi")


# COMMAND ----------

# MAGIC %sql
# MAGIC select "test"
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #Title1
# MAGIC ##Title2
# MAGIC ###Title3
# MAGIC
# MAGIC 1. one
# MAGIC 1. two
# MAGIC
# MAGIC * one
# MAGIC * two

# COMMAND ----------

# MAGIC %run ./Includes/Setup
# MAGIC

# COMMAND ----------

print (full_name)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets
# MAGIC
# MAGIC

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print (files)

# COMMAND ----------

display(files)
