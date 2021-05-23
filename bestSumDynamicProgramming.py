'''
write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as argument.

The function should return an array containing the shortest combination of numbers that add up to esactly the targetSum.
If there is a tie for the shortest combination, you may return any one of the shortest.
bestSum(7,[5,3,4,7]) = > [7]
bestSum(8,[2,3,5]) = > [5,3]
'''


def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestComb = None
    for num in numbers:
        remain = targetSum - num
        res = bestSum(remain, numbers,memo)
        if res != None:
            res.append(num)
            # if the combination is shorter than the shortest then update the veriale
            if shortestComb is None or len(res) < len(shortestComb):
                shortestComb = res
    memo[targetSum] = shortestComb
    return shortestComb


print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [3,5]
print(bestSum(8, [1, 4, 5]))  # [4,4]
print(bestSum(8, [1,2, 3, 5,6,8])) #[2,6]
print(bestSum(100, [1, 2, 5, 25]))  # [25,25,25,25]