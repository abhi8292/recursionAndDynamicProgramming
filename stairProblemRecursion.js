// There are n stairs, a person standing at the bottom wants to reach the top. 
// The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.

var waysToReach = function(N ){
    if(N == 1) return 1
    if(N == 2) return 2
    return waysToReach(N-1) + waysToReach(N-2)
    
}

console.log(waysToReach(1000))