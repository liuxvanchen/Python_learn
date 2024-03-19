import matplotlib.pyplot as plt  # 导入matplotlib库，用于绘图
import seaborn as sns  # 导入seaborn库，基于matplotlib的图形可视化Python库
import pandas as pd  # 导入pandas库，用于数据处理和分析
from sklearn import datasets  # 从sklearn库中导入datasets模块，用于加载数据集

# 加载鸢尾花数据集，三种花，四种特征，150个样本量
iris = datasets.load_iris()

# 打印数据集描述
# print(iris.DESCR) # 可选

# 获取特征数据,是一个（150，4）的numpy数组，150行4列，每一行是一个样本，每一列是一个特征值
X = iris.data

# 获取目标标签，是一个长度为150的一维数组，对应类别标签为0，1，2（三种鸢尾花的标签）
y = iris.target

# 打印特征数据的前5行
print("特征数据前5行:\n", X[:5])

# 打印目标标签的前5个
print("目标标签前5个:\n", y[:5])

# 获取特征名称
feature_names = iris.feature_names
print("特征名称:\n", feature_names)

# 获取目标标签的名称
target_names = iris.target_names
print("目标标签名称:\n", target_names)

# 可视化分析
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['target'] = pd.Series(iris.target)  # 将标签数据转换为dataforme的series类型并且添加到新一列

# 将标签类型0.1.2转化为字符串形式，使用map将键值对
df_iris['target'] = df_iris['target'].map({0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})

# 绘制散点图
# 使用pairlpot函数
# hue指定为那些参数着色，这里是target（类别）
# palette是着色方案，这里是husl方案
# vars指定要绘制的特征列，这里使用iris数据集中的所有特征名称
# diag_kind指定对角线子图类型，kde是核密度估计图，非对角线上面是两种特征值之间的散点图，
sns.pairplot(df_iris, hue="target", palette="muted", vars=iris.feature_names, diag_kind="kde")

plt.show()
