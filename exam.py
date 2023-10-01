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

