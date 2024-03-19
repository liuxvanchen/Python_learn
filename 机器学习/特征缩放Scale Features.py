import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# 一个standardscaler的方法
scale = StandardScaler()
df = pandas.read_csv('D:/浏览器下载/cars.csv')
X = df[['Weight', 'Volume']]
y = df['CO2']

# 对X进行标准化处理，特征缩放
scaledX = scale.fit_transform(X)

# 一个线性回归模型的对象regr
regr = linear_model.LinearRegression()
# 对标准化后的x进行线性拟合
regr.fit(scaledX, y)

# 对要预测的数据进行相同的处理-transform
scaled = scale.transform([[2300, 1.3]])

# ，然后线性拟合
predictedco2 = regr.predict([scaled[0]])
print(predictedco2)
