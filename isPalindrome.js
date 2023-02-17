// function isPalindrome(word){
//     //first variant
//     for (let i = 0; i <= (word.length)/2; i++){
//         if (word[i] != word.at(-i - 1 )){
            
//             return false
//         }
        
//     }

//     return true
// }

//second variant


function isPalindrome(word){
    startLetter = 0
    lastLetter = (word.length)-1
    while (startLetter < lastLetter) {
        if (word[startLetter] != word[lastLetter]){
            return false
        }
        startLetter ++;
        lastLetter --;
    }

    return true
}
console.log(isPalindrome("racecar"))