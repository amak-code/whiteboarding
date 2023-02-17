// Write a function that takes in a string and returns a character count dictionary. 
// For example, "catty" => {"c": 1, "a": 1, "t": 2, "y": 1}

function getCharCount(stringOfWords){
    let countDictionary = {}
    for (const ch of stringOfWords){
        if (ch in countDictionary) {
            countDictionary[ch] += 1
        }
        else{
            countDictionary[ch] = 1
        }
    }

    return countDictionary
}

console.log(getCharCount("catty"))