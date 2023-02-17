// Write a function that takes in a list of strings.
// Return the longest string in the list.

function getLongestString(listOfStrings){
   let maxLength = 0
    let longestWord = ""
    for (const word of listOfStrings) {
        if (word.length > maxLength){
            maxLength = word.length
            longestWord = word
        }
    }

    return longestWord
}

console.log(getLongestString(["apple", "pear", "banana"]))