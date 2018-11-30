# Databricks notebook source
dbutils.widgets.help("dropdown")

# COMMAND ----------

dbutils.widgets.dropdown("X123", "1", [str(x) for x in range(1, 10)])

# COMMAND ----------

dbutils.widgets.get("X123")

# COMMAND ----------

# MAGIC %sql CREATE WIDGET TEXT y DEFAULT "10"

# COMMAND ----------

# MAGIC %sql CREATE WIDGET DROPDOWN cuts DEFAULT "Good" CHOICES select distinct cut from diamonds