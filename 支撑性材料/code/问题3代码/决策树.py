import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing


#from sklearn.model_selection import train_test_split  # 划分训练集与测试集
from sklearn.tree import DecisionTreeClassifier   # 决策树
from sklearn import metrics      # 模型评估模块
import graphviz                # 图形可视化，用户可视化决策树
from sklearn import tree       # sklearn中的树模块，用于导出决策数的dot格式
from sklearn.model_selection import ParameterGrid, GridSearchCV  # 网格搜索


#读取excel
excel=pd.read_excel("决策树数据集.xlsx",sheet_name=0)
#处理缺失值
excel=pd.DataFrame(excel)
data=excel

arr=np.array(excel)
test_int=np.random.choice(67, 17, replace=False)#随机选取测试集
test=[]
for i in test_int:
    test.append(arr[i,:])
test=np.array(test)
train=[]
for i in range(67):
    if i not in test_int:
        train.append(arr[i,:])
train=np.array(train)

y_train,x_train= train[:,0].astype(int), train[:,1:15]
y_test,x_test= test[:,0].astype(int), test[:,1:15]

# 引入决策树模型
clf = DecisionTreeClassifier(criterion='gini'
                             , max_depth=5
                             , random_state=20)
clf.fit(x_train, y_train)  # 模型训练

y_pred = clf.predict(x_test)  # 在测试集上做预测
print(metrics.classification_report(y_test, y_pred))  # 输出分类报告

feature_name = ["是否风化","二氧化硅","氧化钠","氧化钾","氧化钙",
        "氧化铅","氧化钡","五氧化二磷","氧化锶","氧化锡","二氧化硫","钾/硅","铅钡之和/硅","钾/铅钡之和"]  # 特征对应的字段名
# 生成决策树的dot格式
dot_data = tree.export_graphviz(clf
                                , feature_names=feature_name
                                , class_names=["高钾玻璃", "铅钡玻璃"]
                                , filled=True
                                , rounded=True
                                )
#graph = graphviz.Source(dot_data)  # 将决策树进行可视化
graph = graphviz.Source(dot_data.replace('helvetica','"Microsoft YaHei"'), encoding='utf-8')
graph  # 在jupyter 中输出决策树可视化图形

import pydotplus  # 是graphviz的点语言提供了一个python接口

graph1 = pydotplus.graph_from_dot_data(dot_data)
graph1.write_pdf('tree1.pdf')  # 将决策树保存到pdf中

