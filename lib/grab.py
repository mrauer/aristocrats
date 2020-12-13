import requests

DIV_URL = ('https://ycharts.com/charts/fund_data.json?securities='
           'id%3A{}%2Cinclude%3Atrue%2C%2C&calcs='
           'id%3Adividend%2Cinclude%3Atrue%2C%2C&correlations='
           '&format=real&recessions=false&chartView=&splitType='
           'single&scaleType=linear&note=&title=&source=false&units='
           'false&quoteLegend=true&partner=&quotes=&legendOnChart='
           'true&displayTicker=false&ychartsLogo=&useEstimates='
           'false&maxPoints=815')

class Grab:
    def __init__(self):
        pass

    def get_dividends_history(self, ticker):
        r = requests.get(DIV_URL.format(ticker), verify=False)
        return r.text
