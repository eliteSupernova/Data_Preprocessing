import pandas as pd
import numpy as py
from numpy import integer
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('C:\\Users\\1003647\\Desktop\\FLASK_API\\timesheet.csv',encoding='unicode_escape')
df.drop(['Unnamed: 1'],axis=1,inplace=True)
df.drop(1,inplace=True)
df.fillna(value=0,inplace=True)
print(df)
data=df.transpose()
col=data[:1].values
col=[col[0][i].title() for i in range(0,len(col[0]))]
data.columns=col
data.drop('Day',inplace=True)
uni_col=data.columns.unique()
for j in uni_col[1:]:
    val=[sum((i).astype(float)) for i in data[j].values]
    data[j.upper()]=val
data.drop(uni_col[1:],axis=1,inplace=True)
for i in uni_col[1:]:
    print(i,data[i.upper()].sum())
print(data)
# for i in uni_col[1:]:
#     sns.barplot(x=data[i.upper()],y),data=data,label=i)
# plt.show()
# print(data)