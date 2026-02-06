import pandas
from turtle import pd
data = {"Name": ["Ali", "Sara", "Zain"],
 "Age": [21, 22, 20],
 "Grade": ["A", "B", "A"]}
df = pd.DataFrame(data)
print(df)
# Accessing columns
print(df["Name"])
# Accessing row
print(df.loc[1])