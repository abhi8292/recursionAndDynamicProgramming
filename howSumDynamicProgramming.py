'''
Write a function howSum(targetSum, numbers) that take in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return null.
If there are multiple combinations possile, you may return any single one
howSum(7,[5,3,4,7])
'''


def howSum(targetSum, numers, memo = { }):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numers:
        remain = targetSum - num
        result = howSum(remain, numers, memo)
        if result != None:
            result.append(num)
            memo[targetSum] = result
            return result
    memo[targetSum] = None
    return None


print(howSum(7, [2, 3],{}))
print(howSum(7, [5, 3, 4, 7],{}))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5],{}))
print(howSum(300, [7, 14],{}))
