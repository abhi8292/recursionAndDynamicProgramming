


var canSum = function (targetSum, numbers, memo = {}) {

    if (targetSum in memo) return memo[targetSum]
    if (targetSum == 0) return true
    if (targetSum < 0) return false
    for (let num of numbers) {

        remain = targetSum - num
        if (canSum(remain, numbers, memo)){

            memo[targetSum] = true
            return true
        }
    }
    memo[targetSum] = false
    return false
}


console.log(canSum(7, [2, 3])) //True
console.log(canSum(7, [5, 3, 4, 7])) //True
console.log(canSum(7, [2, 4])) //False
console.log(canSum(8, [2, 3, 5])) //True
console.log(canSum(300, [7, 14])) //False