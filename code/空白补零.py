import pandas as pd
import numpy as np

#读取excel
excel=pd.read_excel(r"E:\G\exercise\github\2022_model\excel\表单2处理.xlsx",sheet_name=1)
#处理缺失值
excel=pd.DataFrame(excel)
excel=excel.fillna(value=0)

excel.to_excel(r"E:\G\exercise\github\2022_model\excel\补零的表二数据.xlsx")