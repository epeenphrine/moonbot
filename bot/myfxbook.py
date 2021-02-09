#%%
import requests
import pandas as pd
import datetime
from datetime import datetime, date
import re


def make_req():
    MYFXBOOK_URL = 'https://www.myfxbook.com/forex-economic-calendar'
    res = requests.get(MYFXBOOK_URL).content
    df = pd.read_html(res)
    print(df)
    df_dict = df[0].to_dict('records')
    df_dict_filtered = []
    df_dict_failure = []
    for item in df_dict:
        event_date = item['Date'].split(',')
        event_date_filtered= re.sub('^\s', '', event_date[0])
        try:
            d = datetime.strptime(event_date_filtered,'%b %d')
            d = datetime.strptime(event_date_filtered,'%b %d')
            date_calendar = d.strftime('%m-%d')
            date_today = date.today().strftime('%m-%d')
        except:
            print('probably key error for date time, setting date_calendar and date_today as None')
            date_calendar = None
            date_today =  None

        if date_calendar == date_today and item['Unnamed: 3'].lower() == 'usd':
            print('condition satisfied')
            print(date_calendar)
            print(date_today)
            print(item)
            df_dict_filtered.append(item)
        else: 
            print("================================================")
            print("did not satisfy condition")
            print(item)
            df_dict_failure.append(item)
    print('finished running script')
    return df_dict_filtered 