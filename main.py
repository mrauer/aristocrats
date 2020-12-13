from lib import grab

g = grab.Grab()
div = g.get_dividends_history('ROST')

print(div)
