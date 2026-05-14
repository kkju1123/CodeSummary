

'doesn\'t'  # use \' to escape the single quote...

"doesn't"  # ...or use double quotes instead

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'

print('C:\this\name')  # here \t means tab, \n means newline


print(r'C:\this\name')  # note the r before the quote

import os
path = os.path.join('C:', 'Users', 'Documents')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

'Py' 'thon'  
text = ('Put several strings within parentheses '
        'to have them joined together.')
text

prefix + 'thon'
word[-1]  # last character

word[-2]  # second-last character

word[-6]

word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]  # characters from position 2 (included) to 5 (excluded)

word[:2]   # character from the beginning to position 2 (excluded)

word[4:]   # characters from position 4 (included) to the end

word[-2:]  # characters from the second-last (included) to the end
word[:2] + word[2:]

word[:4] + word[4:]
word[4:42]

word[42:]
word[0] = 'J'
word[2:] = 'py'

squares = [1, 4, 9, 16, 25]
squares
squares[0]  # indexing returns the item

squares[-1]

squares[-3:]  # slicing returns a new list
squares + [36, 49, 64, 81, 100]
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
cubes
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object

rgba.append("Alph")
rgb

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object

rgba.append("Alph")
rgb

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba

rgba

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x

x[0]

x[0][1]

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b