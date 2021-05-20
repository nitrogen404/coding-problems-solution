var checkIfExist = function(arr) {
    const hashMap = {};
    for (let i = 0; i < arr.length; i++) {
        if (hashMap[arr[i]] !== undefined) {
            return true;
        }
        hashMap[arr[i] / 2] = arr[i];
        hashMap[arr[i] * 2] = arr[i];
    }
    return false;
};

console.log(checkIfExist([10, 2, 5, 3, 6]));