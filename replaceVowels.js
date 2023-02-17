// Write a function that takes in a string and 
// returns a string with all vowels replaced with *

function replaceVowels(stringOfWords){
    const vowels = "aeiou"
    let newChars = []
    for (const ch of stringOfWords){
        if (vowels.includes(ch.toLowerCase())){
            newChars.push("*")

        }

        else {
            newChars.push(ch)
        }
        
    }

    return newChars.join("")
}

console.log(replaceVowels("smara"))