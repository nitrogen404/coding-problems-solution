var findDisappearedNumbers = function(nums) {
    let missing = [];
    for (let i = 0; i < nums.length; i++) {
        let pos = Math.abs(nums[i]) - 1;
        if (nums[pos] > 0) {
            nums[pos] *= -1;
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            missing.push(i + 1);
        }
    }
    return missing;

};

console.log(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 1, 3]));