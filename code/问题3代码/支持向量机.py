import pandas as pd
import numpy as np
from joblib import dump, load
from scipy import stats
import seaborn as sns
from sklearn.svm import SVC

sns.set()
from sklearn import svm
import matplotlib.pyplot as plt

#读取excel
excel=pd.read_excel("SVM数据集.xlsx",sheet_name=0)
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


y_train,X_train= train[:,0].astype(int), train[:,2:15]
y_test,X_test= test[:,0].astype(int), test[:,2:15]




#参数 C 的学习曲线

#调线性核函数
# score = []
# C_range = np.linspace(1, 30, 50)
# print(C_range.shape)
# for i in C_range:
#     clf = SVC(kernel="linear", C=i).fit(X_train,y_train)
#     score.append(clf.score(X_test,y_test))
#
# print(max(score), C_range[score.index(max(score))])
# plt.plot(C_range, score)
# plt.show()
#C:软间隔惩罚系数
# C_linear = 1
# model_linear = svm.SVC(C = C_linear, kernel='linear').fit(X_train,y_train) # 线性核
# score=[]
# print(f"Linear Kernel 's score: {model_linear.score(X_test,y_test)}")
# score.append(model_linear.score(X_test,y_test))
# for degree in range(1,10,2):
#     model_poly = svm.SVC(C=1, kernel='poly', degree=degree).fit(X_train,y_train) # 多项式核
#     print(f"Polynomial Kernel with Degree = {degree} 's score: {model_poly.score(X_test,y_test)}")
#     score.append(model_poly.score(X_test, y_test))
#
# for gamma in range(1,10,2):
#     gamma = round(0.01 * gamma,3)
#     model_rbf = svm.SVC(C = 10, kernel='rbf', gamma = gamma).fit(X_train,y_train) # 高斯核
#     print(f"Polynomial Kernel with Gamma = {gamma} 's score: {model_rbf.score(X_test,y_test)}")
#     score.append(model_rbf.score(X_test, y_test))



#model_poly = svm.SVC(C = 10, kernel='poly', degree=3).fit(X_train,y_train) # 多项式核
model_poly = svm.SVC(C = 1, kernel='linear').fit(X_train,y_train) # 线性核
print(model_poly.coef_)
#dump(model_poly, 'SVM模型.joblib')       # 保存
# print(f"s score: {model_poly.score(X_test,y_test)}")
# excel=pd.read_excel("SVM预测.xlsx",sheet_name=0)
# arr=np.array(excel)
# X_pre=arr[:,3:16].astype(float)
# res=model_poly.predict(X_pre)
# print(res)



