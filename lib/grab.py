import json
import os
import string
import time

import requests

NETLOC = os.environ['NETLOC']
COOKIE_FLAG = int(os.environ['COOKIE_FLAG'])
COOKIE_NAME = os.environ['COOKIE_NAME']
COOKIE_VALUE = os.environ['COOKIE_VALUE']

requests.packages.urllib3.disable_warnings()

DIV_URL = ('https://{}/charts/fund_data.json?securities='
           'id%3A{}%2Cinclude%3Atrue%2C%2C&calcs='
           'id%3Adividend%2Cinclude%3Atrue%2C%2C&correlations='
           '&format=real&recessions=false&chartView=&splitType='
           'single&scaleType=linear&note=&title=&source=false&units='
           'false&quoteLegend=true&partner=&quotes=&legendOnChart='
           'true&displayTicker=false&ychartsLogo=&useEstimates='
           'false&maxPoints=815')
TICKERS_URL = ('https://{}/search/data/'
               '?pageNum={}&queryInput={}&searchType=search_companies')
TICKER_MAX_PAGE = 20
TICKERS_FILE = 'data/tickers.json'


class Grab:
    def __init__(self):
        self.cookies = {}
        if COOKIE_FLAG == 1:  # Cookies are set.
            self.cookies = {COOKIE_NAME: COOKIE_VALUE}

    def get_dividends_history(self, ticker):
        r = requests.get(
          DIV_URL.format(NETLOC, ticker),
          verify=False,
          cookies=self.cookies)
        return r.text

    def get_tickers(self):
        ret = {}
        for let in string.printable:
            for i in range(1, TICKER_MAX_PAGE + 1):
                print('Processing {} on page {}. '
                      'Total Tickers={}'.format(let, str(i), len(ret)))
                try:
                    r = requests.get(
                      TICKERS_URL.format(NETLOC, str(i), let), verify=False)
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
