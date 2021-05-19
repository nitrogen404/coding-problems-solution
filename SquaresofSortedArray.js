const sortedSquares = function(nums) {
    let startingPointer = 0;
    let endingPointer = nums.length - 1;
    const newArray = [];
    while (startingPointer != endingPointer) {
        if (nums[startingPointer] * nums[startingPointer] > nums[endingPointer] * nums[endingPointer]) {
            newArray.push(nums[startingPointer] ** 2);
            startingPointer++;
        } else {
            newArray.push(nums[endingPointer] ** 2);
            endingPointer--;
        }
    }
    newArray.push(nums[startingPointer] ** 2);
    
    return newArray.reverse();
};

console.log(sortedSquares([-4, -1, 0, 3, 10]));