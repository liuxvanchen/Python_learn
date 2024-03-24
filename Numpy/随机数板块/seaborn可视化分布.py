#Seaborn 是一个在底层使用 Matplotlib 绘制图形的库。 它将用于可视化随机分布。

import matplotlib.pyplot as plt
import seaborn as sns

# 使用 kdeplot 而不是 displot 来绘制核密度估计图
sns.kdeplot([0, 1, 2, 3, 4, 5])
plt.show()