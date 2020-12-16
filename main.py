import sys

from lib import grab


def main():
    args = sys.argv
    g = grab.Grab()
    if args[1] == 'tickers':
        return g.get_tickers()

    if args[1] == 'dividends':
        return g.get_dividends()


if __name__ == "__main__":
    exit(main())
