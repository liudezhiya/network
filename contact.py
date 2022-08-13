import csv
import os
import re
import time
import pandas as pd
import glob

if __name__ == '__main__':
    year = '2021'

    df_allData = pd.read_csv('G://BaiduNetdiskDownload//135数据//18-22文件整合//'
                             +year+'//alldata_'+year+'.csv',encoding='utf-8',low_memory=False)
    df_author = pd.read_csv('G://BaiduNetdiskDownload//135数据//18-22文件整合//'
                            +year+'//author_'+year+'.csv',encoding='utf-8')
    df_award = pd.read_csv('G://BaiduNetdiskDownload//135数据//18-22文件整合//'
                           +year+'//award_'+year+'.csv',encoding='utf-8')

    #为alldata组合文件id
    df_allData['alldatafileid']=df_allData['alldatafilename']+'_'+df_allData['alldata_uuid']

    #组合alldata和author
    df_allData_author = pd.merge(df_allData, df_author,
                                 left_on='alldatafileid', right_on='authorfilename', how='outer')

    # 组合alldata和award
    df_allData_award = pd.merge(df_allData, df_award,
                                 left_on='alldatafileid', right_on='awardfilename', how='outer')
    #保存
    df_allData_author.to_csv('G://BaiduNetdiskDownload//135数据//18-22文件合并//'
                             +year+'//alldata_author_'+year+'.csv')

    df_allData_award.to_csv('G://BaiduNetdiskDownload//135数据//18-22文件合并//'
                             + year + '//alldata_award_' + year + '.csv')






