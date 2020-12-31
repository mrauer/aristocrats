import json

INPUT_PATH = 'data/dividends.json'
OUTPUT_PATH = 'data/history.json'


class Convert:
    def __init__(self):
        pass

    def convert_data(self):
        data = dict()
        with open(INPUT_PATH, 'r') as infile:
            dividends = json.load(infile)
            for dividend in dividends:
                try:
                    raw_data = (
                        dividends[dividend]['chart_data'][0][0]['raw_data'])
                    data[dividend] = raw_data
                except Exception:
                    pass
        with open(OUTPUT_PATH, 'w') as outfile:
            json.dump(data, outfile)
        return 0
