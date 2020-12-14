import sys

from lib import grab

# div = g.get_dividends_history('PSX')


def main():
    args = sys.argv
    g = grab.Grab()
    if args[1] == 'tickers':
        print(g.get_tickers())


if __name__ == "__main__":
    exit(main())
