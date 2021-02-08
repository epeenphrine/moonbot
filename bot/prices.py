#%%
import requests

def get_prices(ticker):
    """
    get prices from stocktwits api, takes ticker name as param / argument 
    """
    url = f'https://ql.stocktwits.com/batch?symbols={ticker}'
    res = requests.get(url)
    if res.status_code == 200:
        res_json = res.json()
        return res_json
    else: 
        print(f'error in getting requests res code: {res.status_code}')
        return None