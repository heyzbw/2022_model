from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt

# 读入数据
data = pd.read_excel(r"element.xlsx")
data = data[['二氧化硅(SiO2)','氧化钠(Na2O)','氧化钾(K2O)',	'氧化钙(CaO)','氧化镁(MgO)','氧化铝(Al2O3)','氧化铁(Fe2O3)','氧化铜(CuO)','氧化铅(PbO)', '氧化钡(BaO)', '五氧化二磷(P2O5)','氧化锶(SrO)','氧化锡(SnO2)','二氧化硫(SO2)'
]]                    #选择需要的分类特征值
data_Array = data.values                                 #生成数组，以便进行聚类

# 轮廓系数确定K值
def Silhouette_ALL(n):  # 定义的函数
    data_Cluster = KMeans(n_clusters=n)
    data_Cluster.fit(data_Array)
    label = data_Cluster.labels_
    Silhouette_Coefficient = silhouette_score(data_Array, label)
    return Silhouette_Coefficient

y = []
k = []
for n in range(2, 10):  # 遍历不同k值下轮廓系数
    k.append(n)
    data_data_Silhouette_mean = Silhouette_ALL(n)
    y.append(data_data_Silhouette_mean)
print(y)

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.plot(k, y, 'bx-',  color="blue", marker="o", linestyle="--")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.xlabel('K  值', fontsize=14)
plt.ylabel('轮 廓 系 数', fontsize=14)
plt.title('轮 廓 系 数 确 定 K 值', fontsize=14)
plt.show()

