from unittest import case


name = 'keke ju'
name1 = name + 'is good'
name2 = name * 2
print(name)
print(name1)
print(name2)
len0 = len(name)
print(len)

# List
me = ['keke', 'ju', 18, False, 1, 2]
len1 = len(me)
print(len1)
me1 = me[1:3]
print(me1)
me2 = me[-1:-3:-1]
print(me2)

if 1 in me:
    print('1 is in me1')

me.append("python")
me.append([1, 2, 3])
print(me)

user = {'name': 'keke ju', 'age': 18, 'gender': 'male'}
for item , value in user.items():
    print(item, value)
sstr1 = {'keke','ju','python'}
for item in sstr1:
    print(item)

print(list(range(1,10,2)))

print(sum(range(1,10,2)))

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
    else:
        print(f"Found an odd number {num}")

n = 7

#%%
n = 7
for i in range(2, n):
    if n % i == 0:
        print("不是质数"+str(i))
        break
else:
    print("是质数"+str(n))

for i in range(2, 10):
    print(i)
# %%
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def match_args():
    match (x,y):
        case (0,0):
            print("原点")
        case (0,y):
            print(f"y轴上的点，坐标为(0,{y})")
        case (x,0):
            print(f"x轴上的点，坐标为({x},0)")


p = Point(1,2)
match (p,y)
points = [Point(1,2), Point(3,4), Point(5,6)]

match points:
    case[]:
        print("空列表")
    case [Point(1,2)]:
        print(f"一个点，坐标为({1},{2})")
    case [Point(3,4), Point(5,6)]:
        print(f"两个点，坐标分别为({3},{4})和({5},{6})")
    case [Point(x1,y1), Point(x2,y2), *rest]:
        print(f"多个点，前两个点的坐标分别为({x1},{y1})和({x2},{y2})，剩余的点有{len(rest)}个") 


# %%
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def match_args():
        match (x,y):
            case (0,0):
                print("原点")
            case (0,y):
                print(f"y轴上的点，坐标为(0,{y})")
            case (x,0):
                print(f"x轴上的点，坐标为({x},0)")