import pandas as pd
filename = "D:\\WeChat\\WeChat Files\\wxid_lvjv33bjbkg222\\FileStorage\\File\\2024-04\\FLuxnettestdata.csv"
df= pd.read_csv(filename)
print('df的数据类型为:{}'.format(type(df)))
print(df)