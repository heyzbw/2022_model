import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


# 读入数据
plt.plot()
X = pd.read_excel(r"element.xlsx")
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

# 肘部法确定K值
distortions = []
K = range(2, 10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# 绘图
#设置中文格式宋体
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.plot(K, distortions, 'bx-',  color="blue", marker="o", linestyle="--")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.xlabel('K  值', fontsize=14)
plt.ylabel('成 本 函 数', fontsize=14)
plt.title('肘 部 法 确 定 K 值', fontsize=14)
plt.show()
