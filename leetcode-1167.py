'''
leetCode - 1167

Minimum Cose to connect sticks

you have some sticks with positive integer lengths.
you can connect any two sticks of lengths x and y you one stick by paying a cost of x+y.
you perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in the way.

Example 1:
Input: Sticks = [2,4,3]
Output : 14
                Cost
2+3           => 5
5+4           => 9

Total Cost     14

Example 2:
Input: Sticks= [1,8,3,5]
ouput: 30
                Cost
1+3           => 4
4+5           => 9
9+8           => 17

Total Cost      = 4+9+17 => 30

'''
def minimalCost(list):

    if len(list) == 1:
        return list[0]
    list.sort(reverse=True)
    cost = 0
    while len(list)>1:

        x = list.pop()
        y = list.pop()
        new = x+y
        cost += new
        list.append(new)
        list.sort(reverse=True)
    return cost

print(minimalCost([2,4,3]))