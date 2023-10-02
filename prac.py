# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
#
# res = [[0,0,0],
#        [0,0,0],
#        [0,0,0]]
#
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         res[j][i]=mat[i][j]
#
# for r in res:
#     print(r)



# ls1 = [1,2,1,2,4]
# def uniqe(arr):
#     return [ i for i in arr if arr.count(i)<2]
#
# print(uniqe(ls1))

# def fib(n):
#     while not isinstance(n,int):
#         break
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return(fib(n-1)+fib(n-2))
#
#
# print(fib(6))

# def commons(ls1,ls2):
#     list1= set(ls1)
#     list2 = set(ls2)
#     if (list1 & list2):
#         return True
#     else:
#         return False
# ls1 = [1,2,3,4,5]
# ls2 = [3,4,5,6,7]
# print(commons(ls1,ls2))

# def poweroftwo(x):
#
#    return (x and(not(x & (x-1))))
#
# print(poweroftwo(16))


def bitCount(n):
    c = 0
    while(n):
        n &= (n - 1)
        c += 1
    return c

#print(bitCount(11))

def hamm(n):
    count = 0
    while(n):
        n &= (n - 1)
        count += 1
    return count

# def gcd(x, y):
#     while y != 0:
#         (x, y) = (y, x % y)
#     return x
#
# print(gcd(255,300))

# M = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
#
# transposed = [[j[i] for j in M] for i in range(len(M[0]))]
# for row in transposed:
#     print(transposed)

ls = [bool(None),bool('smt'),0,int(), bool()]
ls.sort()
print(ls)

def rec_fac(n):
    if n == 1 or n ==0:
        return 1

    else:
        return n*rec_fac(n-1)

print(rec_fac(5))
