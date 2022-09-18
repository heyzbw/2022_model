import pandas as pd
import numpy as np
from joblib import dump, load
from scipy import stats
import seaborn as sns
from sklearn.svm import SVC

svm=load('SVM模型.joblib')      # 加载

print(svm.coef_)

# for row in X_pre:
#     max=[]
#     origin=svm.predict(row.reshape(1, -1))
#     flag=1
#     for ele in row:
#         max1=[]
#         while(ele<100):
#             ele+=0.1*ele
#             tmp=svm.predict(row.reshape(1, -1))
#             if(tmp!=origin):
#                 max1.append(ele)
#                 flag=0
#                 break
#         if(flag!=0):
#             max1.append(-1)
#         max.append(max1)
# print(max)

