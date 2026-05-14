#%%
class Point:
    __match_args__ = ("x", "y")
    print(__match_args__)
    def __init__(self, x, y):
        self.x = x
        self.y = y

p0 = Point(1,2)
p1 = Point(3, 4)
p = (p0, p1)
match p:
    case (Point(1, 2), Point(3,4) as p2):
        print(f"Point with x={x} and y={y} and p2={p2}")
    case _:
        print("Not a point")
# %%
def httperror(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(httperror(400))
print(httperror(404))
print(httperror(418))
print(httperror(500))

# %%
from enum import Enum, auto
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()  
def colorize(color):
    match color:
        case Color.RED:
            return "red"
        case Color.GREEN:
            return "green"
        case Color.BLUE:
            return "blue"
print(colorize(Color.RED))
print(colorize(Color.GREEN))
print(colorize(Color.BLUE))
# %%
def fib(n):
    a, b = 0, 1
    results = []
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        results.append(a)
    return results

print(fib(10))
# %%
def f(*args):
    print(args)
f(1, 2, 3)
f('a', 'b', 'c')
# %%
def g(**kwargs):
    print(kwargs)
g(name='Alice', age=30)
g(city='New York', country='USA')
# %%
def h(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
h(1, 2, 3, name='Alice', age=30)
# %%
def f(a,/, b, *, c):
    print(f"a={a}, b={b}, c={c}")
f(1, b=2, c=3)
# %%
name = {"first": "John", "last": "Doe"}
def f(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
f(**name)
# %%
list1 = [1, 2, 3, 4, 5]
list1.extend([6, 7, 8])
list1.insert(1,'q')
list1.remove(1)
print(list1.pop(2))
print(list1)
print(list1.index('q'))
print(list1.count("q"))
list1.remove('q')
list1.sort(key=lambda x: (isinstance(x, str), x))
print(list1)
print (list([1, 2, 3,'a', 'b', 'c']))
# %%
list2 = [1, 2, 3, 4, 5,'a', 'b', 'c']
list2.sort(key=lambda x: (isinstance(x, str), x))
print(list2)
print(list(filter(lambda x: isinstance(x, int), list2)))

# %%
# use list as stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
print(stack)

# %%
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft())
print(queue)
# %%
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
new_mat = [[row[i] for row in matrix] for i in range(4)]
print(new_mat)
print(list(zip(*matrix)))
# %%
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
str1 = '{:9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(str1)

# %%
s = 'Hello, world.'
print(str(s))

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# 字符串的 repr() 会添加引号和反斜杠：
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是任何 Python 对象：
repr((x, y, ('spam', 'eggs')))
# %%
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# %%
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# %%
animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')
# %%
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# %%
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# %%
print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))
# %%
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
# %%
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
# %%
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# %%
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# %%
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))
# %%
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# %%
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 请注意上一行中 'end' 的使用
    print(repr(x*x*x).rjust(4))
# %%
'12'.zfill(5)

'-3.14'.zfill(7)

'3.14159265359'.zfill(5)
# %%
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# %%
f = open('workfile', 'w', encoding="utf-8")
# %%
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# 我们可以检测文件是否已被自动关闭。
f.closed
# %%
f.close()
f.read()
# %%
f.read()

f.read()
# %%
f.readline()

f.readline()

f.readline()
# %%
for line in f:
    print(line, end='')
# %%
f.write('This is a test\n')
# %%
value = ('the answer', 42)
s = str(value)  # 将元组转换为字符串
f.write(s)
# %%
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # 定位到文件中的第 6 个字节

f.read(1)

f.seek(-3, 2)  # 定位到倒数第 3 个字节

f.read(1)
# %%
import json
x = [1, 'simple', 'list']
json.dumps(x)
# %%
json.dump(x, f)
# %%
x = json.load(f)
# %%
