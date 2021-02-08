#%%
import requests
import pandas as pd
import bs4 as bs
import json
import time
CHANGE_COLUMNS = ['name', 'last', 'change','change%'] 
CHANGE_COLUMNS_FOREX = ['name', 'last', 'change', 'change%'] 

def make_req_and_make_df_dict(url):
    """
    make requests and then pass to pandas dataframe and then convert to dictionary
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
        }
        res = requests.get(url,headers=headers).content
        df = pd.read_html(res)[0]
        df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low','Time', 'Unnamed: 9'], axis=1, inplace=True)
        df.columns = CHANGE_COLUMNS 
        df_dict =  df.to_dict('records')
        return df_dict 
    except:
        print(f'ran into errors in make_req for URL: {url}')
        return None 
def make_req_and_make_df_dict_forex(url):
    """
    same thing for, but for crypto
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
        }
        res = requests.get(url,headers=headers).content
        df = pd.read_html(res)[0]
        df.drop(columns=["Open", "Unnamed: 0", 'High', 'Low', 'Time'],axis=1, inplace=True)
        df.columns = CHANGE_COLUMNS_FOREX 
        df_dict =  df.to_dict('records')
        return df_dict 
    except:
        print(f'ran into errors in make_req for URL: {url}')
        return None 

def wrangle_data():
    ## regular market stuff
    URLS = [ 
        'https://www.investing.com/indices/indices-futures', #futures
        'https://www.investing.com/currencies/fx-futures', #currency 
        # 'https://www.investing.com/commodities/real-time-futures', #commodity
    ]

    ## crypto
    FOREX_URL ='https://www.investing.com/currencies' 
    df_dict_list = []
    for url in URLS:
        try:
            df_dict = make_req_and_make_df_dict(url)
            df_dict_list.append(df_dict)
        except: 
            print(f'ran into errors trying to get {url}')
            df_dict_list.append(None)
    try:
       df_dict_list.append(make_req_and_make_df_dict_forex(FOREX_URL))
    except:
        print('rand into some error trying to get request for forex')
    data = {
      'dow': None,
      'es': None,
      'nas': None,
      'vix': None,
      'eur/usd': None,
      'gbp/usd': None,
      'usd/jpy': None,
      'usd/chf': None,
      'aud/usd': None,
      'eur/gbp': None,
      'usd/cad': None,
      'nzd/usd': None,
      'eur/jpy': None,
      'gbp/jpy': None,
    }
    FOREX_KEYS = list(data.keys())[4:]
    for df_dicts in df_dict_list:
        if df_dicts:
            ## futures for market stuff
            if not data['dow']:
                data['dow'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'US 30'][0]
            if not data['es']:
                data['es'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'US 500'][0]
            if not data['nas']:
                data['nas'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'US Tech 100'][0]
            if not data['vix']:
                data['vix'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'S&P 500 VIX'][0]

            ## forex crap 
            for FOREX_KEY in FOREX_KEYS:
                if not data[FOREX_KEY]:
                    check_eur_usd = data[FOREX_KEY] = [df_dict for df_dict in df_dicts if df_dict['name'].lower() == FOREX_KEY]
                    if check_eur_usd:
                        data[FOREX_KEY] = check_eur_usd[0]

    return data
testing = wrangle_data()
print(testing)