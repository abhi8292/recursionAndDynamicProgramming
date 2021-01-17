// Write a function canConstruct(target,wordBank) that accepts a target string and an array of strings.

// The function should return a boolean indicating whether or not the target can be constructed by
// concatenating elements of the wordBank array.

// You may reuse elements of wordBank as many times as needed

var canConstruct = function(target,wordBank){
    if (target ===''){
        return true
    }
    for (var word in wordBank){
        if(target.indextOf(word)){
            const suffix = target.slice(word.length)
            if(canConstruct(suffix, wordBank) == true){
                return true
            }
        }
    }
    return false
}