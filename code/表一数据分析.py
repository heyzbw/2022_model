import pandas as pd
import numpy as np

# 打开excel表格
excel=pd.read_excel("附件.xlsx",sheet_name=0)
#转化为numpy数组
arr=np.array(excel)
print(arr)
encoder=[]
for row in arr:
    tmp=[1,2,3,4]
    #对纹饰进行编码
    if row[1]=='A':
        tmp[0]=1
    elif row[1]=='B':
        tmp[0]=2
    else:
        tmp[0]=3
    #类型编码
    if row[2]=="高钾":
        tmp[1]=1
    else:
        tmp[1]=2
    #颜色编码
    if row[3]=='绿':
        tmp[2]=1
    elif row[3]=='黑':
        tmp[2] = 2
    elif row[3]=='深蓝':
        tmp[2] = 3
    elif row[3]=='浅绿':
        tmp[2] = 4
    elif row[3]=='紫':
        tmp[2] = 5
    elif row[3]=='深绿':
        tmp[2] = 6
    elif row[3]=='蓝绿':
        tmp[2] = 7
    elif row[3]=='浅蓝':
        tmp[2] = 8
    else:
        tmp[2]=9
    #风化编码
    if row[4]=="风化":
        tmp[3]=1
    else:
        tmp[3]=2
    encoder.append(tmp)
pd_encoder=pd.DataFrame(encoder)
pd_encoder.to_excel('表一编码结果.xlsx')
