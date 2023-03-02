# ***************** DATA PREPROCESSING OF 'C:\\Users\\1003647\\Desktop\\FLASK_API\\triall.xlsx'
import calendar
# import pandas as pd
# import numpy as np
#
# file='C:\\Users\\1003647\\Desktop\\FLASK_API\\triall.xlsx'
# #
# df=pd.read_excel(file,header=None)
# col=['NaN' if "Unnamed" in i else i for i in df.iloc[0:1,:].values]
# dat=df.transpose()
# dat[0]=dat[0].fillna(method='ffill')
# data=dat.transpose()
# data.columns=dat[0]
# pro=[]
# for i in data.columns[1:]:
#    if i not in pro:
#        pro.append(i)
#
# print(pro)
# data.drop([0],axis=0,inplace=True)
# data=data.fillna(0,axis=0)
# print(data)
# sub_pro=data.iloc[0:1,1:].values
# print('sub',sub_pro)
# id=df.iloc[1:,0:1].values
# new_id=[i[0] for i in id]
# print(new_id)
# final_id=[j for i in range(len(sub_pro[0])) for j in new_id[1:]]
# print(final_id)
# processes=[i for i in data.columns[1:] for j in new_id[1:]]
# #
# # Process=[i for i in proc  for j in range(len(sub_pro[0])*len(id))]
# print(processes)
# sub_process=[i for i in sub_pro[0] for j in new_id[1:]]
# print(sub_process)
# fieldflex=[]
# for i in pro:
#     fieldflex.extend((data[i][1:].values).tolist())
# FLXFIELD=[]
# for i in fieldflex:
#     FLXFIELD.extend(i)
#
# print(len(final_id))
# print(len(processes))
# print(processes)
# print(len(FLXFIELD))
# print(len(sub_process))
# # print(len(final_id))
# final_df={}
# final_df['id']=final_id
# final_df['PROCESS']=processes
# final_df['FLEX_FEILD01']=FLXFIELD
# final_df['SUB_PROCESS']=sub_process
# data=pd.DataFrame(final_df)
# print(data)


# ***************** FIND start date and end date of any given date************************

import datetime
import pandas as pd

in_date='28-07-23'
op_date=datetime.datetime.strptime(in_date,'%d-%m-%y').date()
def start_last_date(dt):
    dt_date = datetime.datetime.strptime(dt, '%d-%m-%y').date()
    str_day=dt_date.day-1
    # str_day=dt_date.relpace(day=1)    **************alternate method
    strt_date=datetime.datetime(dt_date.year,dt_date.month,dt_date.day-str_day).date()
    # l_day=calendar.monthrange(op_date.year,op_date.month)  ****alternate method calendar.monthrange
    # strt_date=pd.Period(dt_date,freq='M').start_time.date()  *****alternate method
    l_day=pd.Period(dt_date,freq='M').end_time.date()
    print(l_day)
    # l_date=datetime.datetime(op_date.year,op_date.month,l_day[1])       ****alternate method calendar.monthrange
    return f'input date : {dt_date} ,start date : {strt_date}, last date : {l_day}'
print(start_last_date(in_date))

# print(op_date)