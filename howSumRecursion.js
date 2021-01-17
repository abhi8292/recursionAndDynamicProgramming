// Write a function howSum(targetSum, numbers) that take in a targetSum and an array of numbers as arguments.
// The function should return an array containing any combination of elements that add up to exactly the targetSum.
// If there is no combination that adds up to the targetSum, then return null.
// If there are multiple combinations possile, you may return any single one

var howSum = function(targetSum, numers){

    if (targetSum == 0) return []
    if (targetSum < 0) return null
    for (var num of numers){
        remain = targetSum - num
        result = howSum(remain, numers)
        if (result !== null){
            result.push(num)
            return result
        }
    }
    return null
}


console.log(howSum(7, [2, 3]))
console.log(howSum(7, [5, 3, 4, 7]))
console.log(howSum(7, [2, 4]))
console.log(howSum(8, [2, 3, 5]))
console.log(howSum(300, [7, 14]))