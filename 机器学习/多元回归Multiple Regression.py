import pandas
from sklearn import linear_model
#读取csv文件
df=pandas.read_csv('D:/浏览器下载/cars.csv')

X=df[['Weight','Volume']]
y=df['CO2']

regr=linear_model.LinearRegression()
regr.fit(X,y)

#预测
# predectedCO2=regr.predict([[2300,1300]])
# print(predectedCO2)

#这些值告诉我们，如果重量增加 1g，则 CO2 排放量将增加 0.00755095g。

#如果发动机尺寸（容积）增加 1 ccm，则 CO2 排放量将增加 0.00780526g。
print(regr.coef_)