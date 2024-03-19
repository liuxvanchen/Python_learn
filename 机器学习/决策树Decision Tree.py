import csv
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv('shows.csv')
# print(df)

# 如需制作决策树，所有数据都必须是数字
d = {'UK': 0, 'USA': 1, 'N': 2}
# map方法接受一个字典，将键转换为值
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']
# 特征值是我们想要通过这些信息来预测
X = df[features]
# y是目标列，我们尝试预测的值
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img = pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
print(dtree.predict([[40, 10, 7, 1]]))
