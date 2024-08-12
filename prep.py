def foo(bar = None):
    if bar is None:
        bar = []
    bar.append(1)
    return bar

# print(foo())
# print(foo())
# print(foo([1,2,3,4]))

def outer(n):
    ls = []
    for i in range(n):
        ls.append(lambda x: x *i)
    return ls

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
# print(foo(ls1))

def repeating_element(ls):
    res = 0
    for i in ls:
        res ^=i
    return res
ls = [1,2,3,1,2]
print(repeating_element(ls))

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

ls3 = list(prev(6))
# print(ls3)

def bar(ls=[]):
    ls.append(("c++",'java'))
    print(ls)
    return ls

# bar()
# bar(['python'])
# bar()

def outer(n):
    for i in range (4):
        yield lambda x:x*n

# res = outer(5)
# for foo in res:
#     # print(foo(3))

ls4 = [bool(None),[1,2,3,4],0,int(),bool(),{'name':'jey',"age":250}]
ls5 = [[1,2,3]]
ls4+=ls5
print(ls4)



result = []
def unpacker(ls):
    for i in ls:
        if type(i) == list :
            unpacker(i)
        else:
            result.append(i)
    return result

print(unpacker(ls))