'''
Problem Statement => You are a traveller on a 2D grid. You egin in top-left corner and your goal is to travel to the
botton-rigt corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m*n?

write a function 'gridTraveler(m, n)' that calculates this.
'''


def gridTraveller(m, n, memo={}):
    key = str(m)+','+str(n)
    if key in memo.keys():
        return memo[key]
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)
    return memo[key]

print(gridTraveller(1, 6))
print(gridTraveller(2, 3))
print(gridTraveller(3, 2))
print(gridTraveller(3, 3))
print(gridTraveller(18, 18))
