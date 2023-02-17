// Write a function that takes in an item and a list. 
// Return the number of times the given item appears in the list.

function countItem(item, listOfItems){
    let counter = 0

    for (const el of listOfItems){
        if (el === item){
            counter ++;
        }
    }

    return counter
}

console.log(countItem(7, [1,2,4,5,1]))