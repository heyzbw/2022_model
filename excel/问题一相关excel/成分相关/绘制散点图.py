import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


excel=pd.read_excel("风化分类.xlsx")#读取文件
excel=pd.DataFrame(excel)
excel=excel.fillna(value=0)#填充nan值

arr=np.array(excel)
chemi=arr[:,5:19]#切片化学成分

#数据分类
k=chemi[0:18,:]
pb=chemi[18:67,:]
#设置中文格式  可以优化好看点
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#创建画布
plt.figure(figsize=(10, 10))
plt.grid(alpha=0.3)#设置透明度
#画散点图
plt.scatter(k[:,3],k[:,9],100, c='red', marker="o",label="高钾玻璃")
plt.scatter(pb[:,3],pb[:,9],100, c='green', marker="o",label="铅钡玻璃")
#图例放置位置
plt.legend(loc='upper right')
plt.xlabel("氧化钾的含量")
plt.ylabel("氧化铅的含量")

plt.show()

