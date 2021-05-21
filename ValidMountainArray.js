var validMountainArray = function(arr) {
     let maxIndex = 0;
     while (arr[maxIndex] < arr[maxIndex + 1]) {
     	maxIndex++;
     }
     if (maxIndex === 0 || maxIndex === arr.length - 1) {
     	return false;
     }
     while (arr[maxIndex] > arr[maxIndex + 1]) {
     	maxIndex++;
     }
     return maxIndex === arr.length - 1 && arr.length > 2;  // returns a boolean value	
};

console.log(validMountainArray([1, 3, 2]));