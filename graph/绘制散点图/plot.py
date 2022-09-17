import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import csv

excel=pd.read_excel("风化分类.xlsx")#读取文件
excel=pd.DataFrame(excel)
excel=excel.fillna(value=0)#填充nan值

arr=np.array(excel)
chemi=arr[:,5:19]#切片化学成分

#数据分类
kf=chemi[0:6,:]
knf=chemi[6:18,:]
pbf=chemi[18:44,:]
pbnf=chemi[44:67,:]
#print(chemi)

#横坐标值
x_kf=range(1,7)
x_knf=range(7,19)
x_pbf=range(19,45)
x_pbnf=range(45,68)
#y轴标签
ylabel=["二氧化硅(SiO2)","氧化钠(Na2O)","氧化钾(K2O)","氧化钙(CaO)","氧化镁(MgO)","氧化铝(Al2O3)","氧化铁(Fe2O3)","氧化铜(CuO)",
        "氧化铅(PbO)","氧化钡(BaO)","五氧化二磷(P2O5)","氧化锶(SrO)","氧化锡(SnO2)","二氧化硫(SO2)"]
#设置中文格式  可以优化好看点
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
for k in range(14):
    #切去要画的化学成分
    ele_kf=kf[:,k]
    ele_knf = knf[:, k]
    ele_pbf = pbf[:, k]
    ele_pbnf = pbnf[:, k]
    #创建画布
    plt.figure(figsize=(10, 10))
    plt.grid(alpha=0.3)#设置透明度
    #画散点图
    plt.scatter(x_kf, ele_kf, s=100, c='red', marker="o",label="高钾风化")
    plt.scatter(x_knf, ele_knf, s=100, c='sandybrown', marker="o",label="高钾未风化")
    plt.scatter(x_pbf, ele_pbf, s=100, c='cyan', marker="o",label="铅钡风化")
    plt.scatter(x_pbnf, ele_pbnf, s=100, c='blue', marker="o",label="铅钡未风化")
    #图例放置位置
    plt.legend(loc='upper right')
    plt.xlabel("文物顺序")
    plt.ylabel(ylabel[k])
    plt.savefig(ylabel[k]+'.png')  # 保存图片
