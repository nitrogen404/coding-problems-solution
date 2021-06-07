// find the unique element in an array. 

const unique_element = function(array) {
    const hashmap = new Map()
    for (num of array) {
        if (!hashmap.has(num)) {
            hashmap.set(num, 1)
        }
        else {
            hashmap.set(num, hashmap.get(num) + 1)
        }
    }

    for (key of hashmap.keys()) {
        if (hashmap.get(key) === 1) {
            return key
        }
    }
}   

console.log(unique_element([7, 5, 9, 2, 9, 5, 7, 6, 6, 1, 0, 1, 0]))