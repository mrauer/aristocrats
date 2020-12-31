import sys

from lib import compute, convert, grab

GRAB_KW = 'grab'
CONVERT_KW = 'convert'
COMPUTE_KW = 'compute'


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

    if args[1] == COMPUTE_KW:
        u = compute.Compute()
        return u.compute_aristocrats()


if __name__ == "__main__":
    exit(main())
