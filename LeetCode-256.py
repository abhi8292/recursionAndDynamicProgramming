'''
LeetCode - 256

Paint House
There a row of n houses each house can be painted iwth one of the three colors. Red blue or green. The cost of painting
each house with a certain color is different. You have to paint all the house3s such that no two adjacent house have the same color.
The coast of painting each house with a certain is represed by a n*3 coast matrix. For example coast[0][0] is the cost
of the paining house 0 with color red costs[1][2] is the cost of painting house 1 with color green and so on Find the
minimum cost to paint all houss.

Note
All costs are positive integers

Ex1 :
input = [[17,2,17],[16,16,5],[14,3,19]]
output = 10

Explanation = Paint House 0 into blue, paint house 1 into green , paint house 2 into blue

Minimum Cost = 2 + 5 + 3 = 10

'''

def findMinCost(cost):

    print(cost)
    if cost == None:
        return None

    for i in range(1,len(cost)):
        cost[i][0] += min(cost[i-1][1],cost[i-1][2])
        cost[i][1] += min(cost[i-1][0],cost[i-1][2])
        cost[i][2] += min(cost[i-1][1],cost[i-1][0])
        print(cost)
    return cost

inp = [[17,2,17],[16,16,5],[14,3,19],[14,3,19],[14,3,19]]
newCost = findMinCost(inp)
size = len(newCost)-1
print(min(newCost[size]))