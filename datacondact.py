import csv
import os
import re
import time
import pandas as pd
import glob

'''将同一目录多个csv文件合成一个csv文件'''
def dataAllToAll(alldata_filenames,df_alldata):
    for alldata_filename in alldata_filenames:  # alldata文件目录遍历
        alldataPureFileName = re.search('[0-9]{4}_[A-Z][0-9]{2}', alldata_filename)
        print('进行到：', alldataPureFileName.group())
        df = pd.read_csv(alldata_filename,index_col=0,encoding='utf-8')
        df['alldatafilename']=alldataPureFileName.group()
        df_alldata = pd.concat([df_alldata, df])
    # 所有alldata记录
    df_alldata.rename(columns={'uuid': 'alldata_uuid'}, inplace=True)
    df_alldata.to_csv('G://data//alldata_'+year+'.csv', index=False, encoding='utf-8')

def authorToAll(author_filenames,df_author):
    for author_filename in author_filenames:  # alldata文件目录遍历
        authorFileName = re.search('[0-9]{4}_[A-Z][0-9]{2}\w*', author_filename)
        author_df = pd.read_csv(author_filename, index_col=0,encoding='utf-8')
        author_df['authorfilename'] = authorFileName.group()
        df_author = pd.concat([df_author, author_df])
        print(df_author)
    # 所有author记录
    df_author.rename(columns={'uuid': 'author_uuid'}, inplace=True)
    df_author.to_csv('G://data//author_'+ year +'.csv', index=False, encoding='utf-8')

def awardToAll(award_filenames,df_award):
    for award_filename in award_filenames:  # alldata文件目录遍历
        awardFileName = re.search('[0-9]{4}_[A-Z][0-9]{2}\w*', award_filename)
        award_df = pd.read_csv(award_filename, index_col=0,encoding='utf-8')
        award_df['awardfilename'] = awardFileName.group()
        df_award = pd.concat([df_award, award_df])
        print(df_award)
    #所有award记录
    df_award.rename(columns={'uuid': 'award_uuid'}, inplace=True)
    df_award.to_csv('G://data//award_'+ year +'.csv', index=False,encoding='utf-8')




if __name__ == '__main__':
    year='2018'

    # 测试文件路径all
    alldata_directory='D://workspace//data//18-22//data_all//'+year
    author_directory='D://workspace//data//18-22//author//'+year
    award_directory='D://workspace//data//18-22//award//'+year


    #创建alldata文件遍历目录
    alldata_filenames = glob.glob(alldata_directory + "\*.csv")
    author_filenames = glob.glob(author_directory + "\*.csv")
    award_filenames = glob.glob(award_directory + "\*.csv")

    df_alldata = pd.DataFrame()
    df_author = pd.DataFrame()
    df_award = pd.DataFrame()

    # dataAllToAll(alldata_filenames, df_alldata)
    # authorToAll(author_filenames, df_author)
    awardToAll(award_filenames, df_award)













