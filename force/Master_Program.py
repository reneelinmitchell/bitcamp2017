# coding: utf-8

# In[6]:

import pandas as pd
import ast
from datetime import datetime
from collections import namedtuple
import os


# In[7]:

df_list = []
root = 'C:/Users/cpgei/bitcamp/final_data'
file_list = os.listdir(root)
for i in file_list:
    df_list.append(pd.read_csv(i,encoding='ISO-8859-1',sep='|',names=['advisor','current_company','disclosures','company_history','start','end','company_location']))


# In[8]:

def users_in_common(dataf,name,current_file):
    
    def col2list(df,col):
        #print(df['advisor'][0])
        new_col = []
        count = 0
        #print(col)
        for i in df[col]:
            try:
                new_col.append(ast.literal_eval(i))
                count += 1
            except:
                new_col.append([])
        ser = pd.Series(new_col)
        df[col] = ser   

    def date_diff(date1,date2,date11,date22):
        Range = namedtuple('Range', ['start','end'])
        #date1 = '07/1993'.split('/')
        date1 = date1.split('/')
        date2 = date2.split('/')
        if int(date1[0]) > int(date2[0]) and int(date1[1]) > int(date2[1]):
            f = date1
            date1 = date2
            date2 = f
        date11 = date11.split('/')
        date22 = date22.split('/')
        r1 = Range(start=datetime(int(date1[1]), int(date1[0]), 14), end=datetime(int(date2[1]), int(date2[0]), 14))
        r2 = Range(start=datetime(int(date11[1]), int(date11[0]), 14), end=datetime(int(date22[1]), int(date22[0]), 14))
        latest_start = max(r1.start, r2.start)
        earliest_end = min(r1.end, r2.end)
        overlap = (earliest_end - latest_start).days + 1
        return overlap

    def name_index(name):
        global df
        for index in range(0,len(list(df['advisor']))):
            i = list(df['advisor'])[index]
            if name.lower() == str(i).lower():
                return list(df['advisor']).index(name)

    def how_long(name): # is this function supposed to take another name
        global df
        """Checks how long a certain has worked with who?"""
        in_common = []
        #input_name_index = name_index(name)
        #input_name_index = list(df['advisor']).index(name)
        #print(len(company_history))
        for company_input_index in range(0,len(company_history)):
            company_input = company_history[company_input_index]
            #print('hey')
            for advisor_index in range(0,len(df['advisor'])):
                #print('hey')
                if company_input in df['company_history'][advisor_index]:
                   
                    if company_locations[company_input_index] in df['company_location'][advisor_index]:
                        
                        advisor_matching_index = df['company_location'][advisor_index].index(company_locations[company_input_index])
                        date1 = date1_list[company_input_index]
                        date2 = date2_list[company_input_index]
                        date11 = df['start'][advisor_index][advisor_matching_index]
                        date22 = df['end'][advisor_index][advisor_matching_index]
                        dd = date_diff(date1, date2, date11, date22)
                        if dd >= 1:
                            in_common.append(str(df['advisor'][advisor_index]) + ':' + str(dd))
        return in_common
    df = dataf
    
    
    global desired_user
    if (name in list(df['advisor'])) and (desired_user is None):
        print('Yahoooo!!')
        name_index = list(df['advisor']).index(name)
        #print(name_index)
        desired_user = df[name_index:name_index+1]
        #print(desired_user)
        return ['found it']
    elif desired_user is None:
        return ['not it']
    #print(desired_user)
    company_history = list(desired_user['company_history'])[0]
    company_locations = list(desired_user['company_location'])[0] 
    date1_list = list(desired_user['start'])[0]
    date2_list = list(desired_user['end'])[0]
    
    change_list = ['company_history','start','end','company_location']
    for i in change_list:
        col2list(df,i)
    
    #print(company_history)
        
    return how_long(name)


# In[9]:

input_name = 'STEVEN ROY WILLIAMSON'
total_in_common = []
current_file = 0
#global desired_user
desired_user = None
while current_file <= len(df_list) - 1:
    print('Df Count:' + str(current_file))
    df = df_list[current_file]
    total = users_in_common(df, input_name, current_file)
    print(total)
    if total == ['not it']:
        current_file += 1
    elif total == ['found it']:
        current_file = 0
    else:
        for i in total:
            total_in_common.append(i)
        current_file += 1


# In[10]:

print(total_in_common)