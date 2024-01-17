def enumerrate(item,start=0):
    if hasattr(item, '__iter__'):
        for i in item:
            yield start,i
            start +=1
    else:
        print('obj is not iterable')

ls = [1,2,3,4,5]
ls2 = 5
print(list(enumerrate(ls)))

# def memorize(func):
#     mem = []
#     def inner(*args,**kwargs):
#         x = func()
#         if args in mem:
#             return mem[args]
#         else:
#             func[args] = mem[args]
#         return x
#     return inner

def make_multiplier(n):
    def multiply(x):
        yield lambda n: lambda x: x*n
    return multiply

# y = make_multiplier(3)
# print(y(10))

def foo(*args,**kwargs):
    if len(args) == 1:
        return args[0]*args[0]
    # elif i in range(0,args,2):
    #     return args[i]*args[i+1]
    elif len(args)>1:
        return args[0]*args[1]
    elif kwargs:
        return args,kwargs

# print(foo(name ='dick',age =25))


def factoral(n):

    if n == 1:
        return 1
    elif n>1:
        return n * factoral(n-1)

# x= factoral(5)
# print(x)

ls = [4,1,2,1,2]
res = ls[0]
for i in ls[1:]:
    res ^= 1
print(res)


def duplicates(str):
    let = 0
    for i in str:
        pos = ord(i)
        if let &(1<<pos) > 0:
            print('true')
            break
        let = let | (1<<pos)
    else:
        print('false')
    # dupes = []
    # for i in str:
    #     if str.count(i)>1 and i not in dupes:
    #         dupes.append(i)
    # if len(dupes)>0:
    #     return True
    # else:
    #     return False

    # if len(set(str)) == len(str):
    #     return False
    # else:
    #     return True
# x = duplicates('hello')
# print(x)

# def log_function_info(func):
#     def inner(*args,**kwargs):
#         if args:
#             print(f"{func.__doc__}\n{func.__name__}:{args}\n{log_function_info.__name__}")
#         if kwargs:
#             print(f"{func.__doc__}\n{func.__name__}:{kwargs}\n{log_function_info.__name__}")
#     return inner

# @log_function_info
# def add(x,y):
#     """this function adds two args"""
#     return x+y
# res1 = add(3,4)
# res2 = add(x = 5,y = 4)
# print(res1)

def reversebits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= n & 1
        n>>=1
    return result

# print(reversebits(43261596))

def decimaltobinary(n):
    if n >= 1:
        decimaltobinary(n//2)
    print(n % 2,end='')
# print(decimaltobinary(20))

def binarytodecimal(binary):
    decimal = 0
    i = 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec *pow(2,i)
        binary = binary//10
        i += 1
    print(decimal)

# print(binarytodecimal(10100))

def changing(**kwargs):
    kwargs['lists'][0][1]='kkk'
    print(kwargs)

changing(lists = [[1]*2]*3)

def foo(ls):
    if len(ls)>0:
        return ls.sort()
    else:
        print('list is empty')

ls1 = [ i for i in range(0,5)]
print(foo(ls))