// [0,1,0,3,12]
// [1,3,12,0,0]

var moveZeroes = function(nums) {
    let readpointer = 0;
    for (let writepointer = 0; writepointer < nums.length; writepointer++) {
        if (nums[writepointer] != 0) {
            [nums[readpointer], nums[writepointer]] = [nums[writepointer], nums[readpointer]];
            readpointer++;
        }
    }
    return nums;
};

console.log(moveZeroes([1, 0, 0, 3, 12]));
    