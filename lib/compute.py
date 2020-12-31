import csv
import json
from datetime import datetime

from dateutil.relativedelta import relativedelta

INPUT_PATH = 'data/history.json'
OUTPUT_PATH = 'data/aristocrats.csv'
LARGE_VALUE = 1000000

LABELS = {25: 'aristocrat',
          24: 'emperor',
          23: 'monarch',
          22: 'king',
          21: 'sultan',
          20: 'baron',
          19: 'caesar',
          18: 'caliph',
          17: 'majesty',
          16: 'pasha',
          15: 'prince',
          14: 'emir',
          13: 'notable',
          12: 'vip',
          11: 'eminence',
          10: 'celebrity',
          9: 'estimable',
          8: 'exemplary',
          7: 'reputable',
          6: 'priceless',
          5: 'precious',
          4: 'inestimable',
          3: 'valuable',
          2: 'appreciated',
          1: 'respected',
          0: 'regular'}


class Compute:
    def __init__(self):
        pass

    def compute_aristocrats(self):
        today = datetime.today()
        with open(OUTPUT_PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            with open(INPUT_PATH, 'r') as infile:
                dividends = json.load(infile)
                for idx, dividend in enumerate(dividends):
                    data = dividends[dividend]
                    data.reverse()
                    previous_value = LARGE_VALUE
                    for item in data:
                        if item[1] > previous_value:
                            timestamp = str(item[0])[:10]
                            dt = datetime.fromtimestamp(int(timestamp))
                            years_diff = relativedelta(today, dt).years
                            if years_diff < 0:
                                break
                            writer.writerow([dividend, timestamp, years_diff,
                                             LABELS[years_diff]])
                            print('{} -> {} ({} yrs)'.format(
                                dividend, LABELS[years_diff], years_diff))
                            break
                        previous_value = item[1]
            return 0
