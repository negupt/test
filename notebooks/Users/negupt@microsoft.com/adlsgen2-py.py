# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "35492515-75b3-4487-81b3-81e43ceb30ef",
           "fs.azure.account.oauth2.client.secret": "I2Ilbt5rI9i3tsliK1cNTJ7CMPlFP7U1h/MWXKskfPU=",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/token"}

# Optionally, you can add <your-directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://filesystem1@adlsgen22222.dfs.core.windows.net/",
  mount_point = "/mnt/adlsgen2",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.ls("mnt/adlsgen2"))

# COMMAND ----------

# MAGIC %sh wget -P /tmp https://raw.githubusercontent.com/Azure/usql/master/Examples/Samples/Data/json/radiowebsite/small_radio_json.json

# COMMAND ----------

dbutils.fs.cp("file:///tmp/small_radio_json.json", "mnt/adlsgen2")

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS radio_sample_data;
# MAGIC CREATE TABLE radio_sample_data
# MAGIC USING json
# MAGIC OPTIONS (
# MAGIC  path  "mnt/adlsgen2/small_radio_json.json"
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from radio_sample_data

# COMMAND ----------

display(dbutils.fs.ls("mnt/adlsgen2/folder1"))

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS mainstream_us;
# MAGIC CREATE TABLE mainstream_us
# MAGIC USING csv
# MAGIC OPTIONS (
# MAGIC  path  "mnt/adlsgen2/folder1/ALLMainUS.csv"
# MAGIC )

# COMMAND ----------

# MAGIC %sql Select * from mainstream_us