"""Tuples used as records"""

lax_coordinates = (33.9425, -118.40805)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8012)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s %s' % passport)

""" The for loop knows how to retrieve the items of a tuple separately—this is called
“unpacking.” Here we are not interested in the second item, so it’s assigned to
_ , a dummy variable"""

for country, _ in traveler_ids: # _ is dummy var, “unpacking.”
    print(country)

""" Tuple Unpacking """
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # tuple unpacking
print(latitude)
print(longitude)

t = (20, 8)
mod_data = divmod(*t)
print(mod_data) 

""" Using * to grab excess items"""

a, b, *rest = range(5)
print(a, b, rest) # * return value with list if have

a, *body, c, d = range(5)
print(a, body, c, d) # body [1,2], a, b, c every 1 value and left value for body

""" Nested Tuple Unpacking """
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))

fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: 
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))

""" Named Tuples """
print('namedtuple')
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates') # city class
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) # obj with constructor

# You can access the fields by name or position.
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,139.691667))

print(tokyo.population) 
print(tokyo.coordinates)
print(tokyo[1])