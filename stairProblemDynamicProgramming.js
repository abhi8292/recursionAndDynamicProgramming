// There are n stairs, a person standing at the bottom wants to reach the top. 
// The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.

var waysToReach = function(N , memo={}){
    if(N in memo) return memo[N]
    if(N == 1) return 1
    if(N == 2) return 2
    var res = waysToReach(N-1, memo) + waysToReach(N-2, memo)
    memo[N] = res
    return res
}

console.log(waysToReach(1000))