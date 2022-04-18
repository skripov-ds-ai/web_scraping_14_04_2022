import pandas as pd

# pip install pandas

fruits = [{"type": "apple", "count": 3}, {"type": "orange", "count": 30}]


df = pd.DataFrame.from_records(fruits)
# df = pd.DataFrame()
# df["type"] = [""]
# print(df)
# df.to_csv("df.csv")
df.to_csv("df.csv", index=False)

# data = pd.read_csv("df.csv", index_col=0)
data = pd.read_csv("df.csv")
print(data)

# избегайте бана от сайта! не нужно в этом примере!
# time.sleep(1)
