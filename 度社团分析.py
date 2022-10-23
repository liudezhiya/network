# -*- coding: utf-8 -*-

# @File    : 度社团分析.py
# @Date    : 2022-10-22 17:27  
# @Author  : 刘德智
# @Describe  :
import csv
import os
import re
import time
import pandas as pd
import glob
import pypinyin
import warnings
warnings.filterwarnings('ignore')

def plt_degree(name,degree):
    import matplotlib.pyplot as plt
    year = [2018, 2019, 2020, 2021]
    plt.plot(year, degree, 'b-o')
    plt.xticks(year)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel("年份")
    plt.ylabel("度")
    plt.title(name)
    plt.show()

path='G://BaiduNetdiskDownload//135数据//gephi数据//'

data=pd.DataFrame()
for year in range(2018,2022):
    data_year = pd.read_csv(path + str(year) + '.csv')
    data_year['year'+str(year)] = str(year)
    data=pd.concat([data,data_year],axis=0)
# print(data.columns)
drar_data=data[['Id','Label','type','degree','position',
            'year2018','year2019', 'year2020', 'year2021','timenumber']]
drar_data.fillna(0, inplace=True)
drar_data=drar_data.replace('NaN',0)
# print(drar_data)
# print(drar_data.isnull().sum()/drar_data.shape[0])

#选出四年都出现过的节点
datat_4=drar_data[drar_data['timenumber']==4]

node_degree={}
#drar_data  datat_4

for arow in drar_data.itertuples(index=True, name='Pandas'):
    value=[0,0,0,0]
    key = getattr(arow, "Id")
    dataname = drar_data[drar_data['Id'] == key]
    # dataname = drar_data[drar_data['Id'] == key]
    temp=[]
    for row in dataname.itertuples(index=True, name='Pandas'):
        if getattr(row, "year2018") =='2018':
            value[0]=getattr(row, 'degree')
        # else:
        #     value[0]=0
        if getattr(row, "year2019")=='2019':
            value[1]=getattr(row, 'degree')

        if getattr(row, "year2020")=='2020':
            value[2]=getattr(row, 'degree')

        if getattr(row, "year2021")=='2021':
            value[3]=getattr(row, 'degree')

    node_degree[key]=value
# print(node_degree)
df = pd.DataFrame(pd.Series(node_degree), columns=['degree'])
df = df.reset_index().rename(columns={'index':'name'})
# df.to_csv('度分布2018-2021都出现.csv',index=None)


for row in df.itertuples(index=True, name='Pandas'):
    degree=getattr(row, "degree")

    # if degree[0]<=degree[1]<=degree[2]<=degree[3]:
    #     print('成长社区',getattr(row, "name"),degree)#张悦 [11, 11, 22, 93]

    # if degree[0]>=degree[1]>=degree[2]>=degree[3]>=5:
    #     print('萎缩社区',getattr(row, "name"),degree)#姜奇 [41, 17, 15, 9]

    # if degree[0]>=degree[1]>=degree[2] and degree[3]==0:
    #     print('消失',getattr(row, "name"),degree)#黄欣沂 [108, 0, 0, 0]

    if degree[0]==0 and degree[1]<=degree[2]<=degree[3]:
        print('出生社区',getattr(row, "name"),degree)#刘敬贤 [0, 0, 8, 31]