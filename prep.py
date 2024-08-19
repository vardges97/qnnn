def foo(bar = None):
    if bar is None:
        bar = []
    bar.append(1)
    return bar

# print(foo()),"""1"""
# print(foo()),"""1"""
# print(foo([1,2,3,4])),"""1,2,3,4,1"""

def outer(n):
    ls = []
    for i in range(n):
        ls.append(lambda x: x *i)
    return ls
"""12,12,12,12,12"""
# res = outer(5)
# for foo in res:
#     print(foo(3))

def string_count(str):
    di = {}
    for i in str:
        if i in di:
            di[i] +=1
        else:
            di[i] = 1
    return di

# print(string_count('hello'))

def sumofnums(n):
    if n == 0:
        return 0
    return (n%10 +sumofnums(int(n/10)))
# print(sumofnums(123))

def foo(n):
    res = 0
    if n > 0:
        foo(n-1)
        print(n)

# print(foo(5))


a = [[]]*3
a[1].append(1)
"""[[1],[1],[1]]"""
# print(a)

def process_data(*args, **kwargs):
  if len(args) == 1 and isinstance(args[0], int):
    return args[0] ** 2
  elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
    return args[0] * args[1]
  elif kwargs:
    return kwargs

# print(process_data(name = 'me',age = 23))


def foo(ls):
    if len(ls)>0:
        return ls.sort()
    else:
        print('list is empty')

ls1 = [ i for i in range(0,5)]
"""returns none because ls.sort just sorts"""
# print(foo(ls1))

def repeating_element(ls):
    res = 0
    for i in ls:
        res ^=i
    return res
ls = [1,2,3,1,2]
# print(repeating_element(ls))

def targetfinder(list,target):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]+ls[j]==target:
                return [i],[j]
        else:
            print("no such pair found")

lis=[1,2,3,4,5]
x = targetfinder(lis,5)
# print(x)

def prev(n):
    for i in range(n):yield i
    for i in (x**2 for x in range(n)): yield i

"""from 0 to 5 and from 0 to 25(everything squared)"""
ls3 = list(prev(6))
# print(ls3)

def bar(ls=[]):
    ls.append(("c++",'java'))
    print(ls)
    return ls
"""[('c++', 'java')],[python('c++', 'java')],[('c++', 'java'),('c++', 'java')]"""
# bar()
# bar(['python'])
# bar()

def outer(n):
    for i in range (4):
        yield lambda x:x*n

"""15,15,15,15"""
# res = outer(5)
# for foo in res:
#     print(foo(3))

ls4 = [bool(None),[1,2,3,4],0,int(),bool(),{'name':'jey',"age":250}]
ls5 = [[1,2,3]]
"""adds [1,2,3] at the end"""
ls4+=ls5
# print(ls4)



result = []
def unpacker(ls):
    for i in ls:
        if type(i) == list :
            unpacker(i)
        else:
            result.append(i)
    return result

# print(unpacker(ls))

ls7 =[1,2,3,3,4]
def repelem(ls):
    for i in range(len(ls)):
        if ls[i] == ls[i-1]:
            return True
        else:
            False
print(repelem(ls7))


x = [[i+(j*3) for i in range(1,4)]for j in range(0,3)]
# print(x)

import functools
from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
# print(fib(10))

fact = lambda x: 1 if x == 0 else x * fact(x-1)
"""you can have a recursion with lambda if you name the lambda"""
def sumofnums(num):
    if num ==0:
        return 0
    return (num%10+sumofnums(int(num/10)))

# s= 'a\0b\0c\0d'
# print(len(s))
# print(s)#7
# s += 0#err
# print(s)#contents
# print(len(s))#7

mat =[[1,2,3],[4,5,6],[7,8,9]]
n =3
def matdiagonal(mat,n):
    principal = 0
    sec = 0
    for i in range(0,n):
        for j in range(0,n):
            if (i==j):
                principal+= mat[i][j]
            if (i+j) == (n-1):
                sec += mat[i][j]
    return sec
# print(matdiagonal(mat,n))

def outer(n):
    for i in range(4):
        yield lambda x:x*n
# prints 15,15,15,15 in range of 4 3*15
res = outer(5)
for foo in res:
    print(foo(3))


def sorter(ls):
    for i in range(0,len(ls)):
        for j in range(i+1,len(ls)):
            if i >= j:
                ls[i],ls[i] = ls[j],ls[i]


ls = [bool(None), bool('muchacha'), 0, int(), bool()]
ls.sort()
# print(ls)

# def custom_filter(fn, iterable):
#   res = []

#   if fn is None:
#     for item in iterable:
#       if item == True:
#         res.append(item)
#   else:
#     for item in iterable:
#       if fn(item):
#         res.append(item)
#   return res

def memorize(fn):
  cache = {}
  def wrapper(*args, **kwargs):

    key = str(args)
    key = key + str(kwargs)
    if cache.get(key):
      return cache.get(key)
    result = fn(*args, **kwargs)
    cache[key] = result
    return result
  wrapper.cache = cache


#better way
def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner


ls8 = [bool(None),[1,2,3,4],0,int(),bool(),{'name':'james',"age":23}]
lis=[[1,2,3]]
ls8 += lis
print (ls8)
