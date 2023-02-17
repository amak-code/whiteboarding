// Write a function that takes in a string and 
// returns all unique characters in the string

function getUniqueChars(stringOfWords){

    return Array.from(new Set(stringOfWords))
}

console.log(getUniqueChars("aplle eats pear"))