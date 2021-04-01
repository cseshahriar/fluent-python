colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tsharts = [
    (color, size) 
    for color in colors # 0, 1
    for size in sizes # 0, 1, 2
]
print(tsharts) # tuples in list
"""
[
    ('black', 'S'), 
    ('black', 'M'), 
    ('black', 'L'),
    ('white', 'S'),
    ('white', 'M'),
    ('white', 'L')
] 3 x 2 = 6
"""
print('for loop')
for color in colors:
    for size in sizes:
        print((color, size)) # tuples 

print('list comprehension')
tsharts = [(color, size) for size in sizes for color in colors]
print(tsharts) # tuples in list