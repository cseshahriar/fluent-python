""" Listcomps No Longer Leak Their Variables """
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols] # ord is for orders 
print(codes)

x = 'ABC'
dummy = [ord(x) for x in x] # ord return numeric value of abc
print(x)
print(dummy) 

""" Listcomps Versus map and filter """
print('Listcomps Versus map and filter')
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127] # faster for not casting
print(beyond_ascii)

beyond_ascii = list(filter(lambda c:c > 127, map(ord, symbols)))
print(beyond_ascii)

""" Cartesian Products """