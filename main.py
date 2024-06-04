import polars as pl


pl.Config.set_tbl_rows(100)
pl.Config.set_tbl_cols(10)


df = pl.read_csv("data_1.csv", has_header=True, infer_schema_length=10000)

df_1 = df.filter(pl.col('edycja') == 2021)
df_2 = df.filter(pl.col('edycja') == 2019)


print(df_1.shape)
print(df_2.shape)

