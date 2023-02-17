function add_to_zero(listOfNums) {
    // linear time complexity while using Set()
    const setOfNUms = new Set(listOfNums)

    for (const i of listOfNums){
        if (i === 0 || -i in setOfNUms){
            return true
        }
    }
    return false
}

console.log(add_to_zero([1,2,1]))