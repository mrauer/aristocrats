import json
import string
import time

import requests

requests.packages.urllib3.disable_warnings()

DIV_URL = ('https://ycharts.com/charts/fund_data.json?securities='
           'id%3A{}%2Cinclude%3Atrue%2C%2C&calcs='
           'id%3Adividend%2Cinclude%3Atrue%2C%2C&correlations='
           '&format=real&recessions=false&chartView=&splitType='
           'single&scaleType=linear&note=&title=&source=false&units='
           'false&quoteLegend=true&partner=&quotes=&legendOnChart='
           'true&displayTicker=false&ychartsLogo=&useEstimates='
           'false&maxPoints=815')
TICKERS_URL = ('https://ycharts.com/search/data/'
               '?pageNum={}&queryInput={}&searchType=search_companies')
TICKER_MAX_PAGE = 20
TICKERS_FILE = 'data/tickers.json'


class Grab:
    def __init__(self):
        pass

    def get_dividends_history(self, ticker):
        r = requests.get(DIV_URL.format(ticker), verify=False)
        return r.text

    def get_tickers(self):
        ret = {}
        for let in string.printable:
            for i in range(1, TICKER_MAX_PAGE + 1):
                print('Processing {} on page {}. '
                      'Total Tickers={}'.format(let, str(i), len(ret)))
                try:
                    r = requests.get(
                      TICKERS_URL.format(str(i), let), verify=False)
                    data = r.json()
                    for item in data['results']:
                        key = item['search_id']
                        if key not in ret:
                            ret[key] = item
                    time.sleep(4)
                except Exception:
                    time.sleep(4)
                    continue
        with open(TICKERS_FILE, 'w') as outfile:
            json.dump(ret, outfile)
        return 0
