symbols = '$¢£¥€¤'
tupe_data = tuple(ord(symbol) for symbol in symbols)
print(tupe_data)

import array
array_data = array.array('I', (ord(symbol) for symbol in symbols))
print(array_data)

""" Cartesian product in a generator expression """
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)