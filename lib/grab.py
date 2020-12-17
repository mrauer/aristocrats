import inspect
import json
import os
import random
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
DIVIDENDS_FILE = 'data/dividends.json'
DIVIDENDS_PAUSE_SECONDS = random.randint(7, 19)
DIVIDENDS_PER_BATCH_NUM = 5
SAMPLE_TICKER = 'KO'
CONNECTION_CHECK_MOD = 3


class Grab:
    def __init__(self):
        self.cookies = {}
        if COOKIE_FLAG == 1:  # Cookies are set.
            self.cookies = {COOKIE_NAME: COOKIE_VALUE}

    @property
    def dividends(self):
        dividends = {}
        try:
            with open(DIVIDENDS_FILE, 'r') as infile:
                dividends = json.load(infile)
        except Exception:
            pass
        return dividends

    @property
    def tickers(self):
        tickers = {}
        try:
            with open(TICKERS_FILE, 'r') as infile:
                tickers = json.load(infile)
        except Exception:
            pass
        return tickers

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

    def get_raw_data(self, data):
        return data['chart_data'][0][0]['raw_data']

    def is_connected(self):
        try:
            unauthed = len(
                self.get_raw_data(
                    self.get_dividend(SAMPLE_TICKER, {})))
            authed = len(
                self.get_raw_data(
                    self.get_dividend(SAMPLE_TICKER, self.cookies)))
            if authed > unauthed:
                return True
        except Exception:
            return False
        return False

    def get_dividend(self, ticker, cookies):
        data = {}
        if inspect.stack()[1][3] != 'is_connected':
            print('Processing {}'.format(ticker))
        try:
            r = requests.get(
                DIV_URL.format(NETLOC, ticker),
                verify=False,
                cookies=cookies)
            data = r.json()
        except Exception:
            return
        return data

    def get_dividends(self):
        dividends = self.dividends
        original_len = len(dividends)
        print('{} dividends in total'.format(len(dividends)))
        for idx, ticker in enumerate(self.tickers.keys()):
            if ticker not in dividends.keys():
                data = self.get_dividend(
                    ticker, self.cookies)
                dividends[ticker] = data
                time.sleep(DIVIDENDS_PAUSE_SECONDS)
                if ((idx + 1) % CONNECTION_CHECK_MOD) == 0:
                    print('--connected {}'.format(self.is_connected()))
            if idx + 1 == original_len + DIVIDENDS_PER_BATCH_NUM:
                with open(DIVIDENDS_FILE, 'w') as outfile:
                    json.dump(dividends, outfile)
                return 0
