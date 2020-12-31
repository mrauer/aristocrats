import sys

from lib import convert, grab

GRAB_KW = 'grab'
CONVERT_KW = 'convert'


def main():
    args = sys.argv
    g = grab.Grab()
    if args[1] == GRAB_KW and args[2] == 'tickers':
        return g.get_tickers()

    if args[1] == GRAB_KW and args[2] == 'dividends':
        return g.get_dividends()

    if args[1] == CONVERT_KW:
        c = convert.Convert()
        return c.convert_data()


if __name__ == "__main__":
    exit(main())
