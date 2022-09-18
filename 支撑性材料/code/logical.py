import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
# data=pd.read_csv('Dry_Bean_Dataset.csv')
data = pd.read_excel('C:\\Users\\lenovo\\Desktop\\myworkspace\\mydata.xlsx',sheet_name="Sheet1")
df=pd.DataFrame(data)
Y_train=[]
for i in df['Class'][0:20]:
    if i=='无风化':
        Y_train.append(0)
    else:
        Y_train.append(1)
si=df['si'][0:20]
k=df['k'][0:20]
ca=df['ca'][0:20]
mg=df['mg'][0:20]
al=df['al'][0:20]
fe=df['fe'][0:20]
p=df['p'][0:20]
X_train=list(zip(si,k,ca,mg,al,fe,p))

from sklearn.linear_model import LinearRegression # 导入sklearn库中的线性回归模块
lr = LinearRegression()                           # 定义一个线性回归模型
lr.fit(X_train, Y_train)                          # 将模型拟合到数据上

# y_pred = lr.predict(X_train)
# print(y_pred[:19])

def sigmoid_function(z):
    fz = []
    for num in z:
        fz.append(1/(1 + math.exp(-num)))
    return fz

# 输出w权值
print(lr.coef_)
print(lr.intercept_)

# 载出预测值
y_pred = lr.predict(X_train)
out_y = pd.DataFrame(y_pred)
out_y.to_excel("y_k_pred.xlsx")
# print(y_pred[:])
# x1 , x2 , x3 , x4 , x5 , x6 = X_train[0],X_train[1],X_train[2],X_train[3],X_train[4],X_train[5]

# 验证准确度
score = lr.score(X_train,Y_train)
print(score)
