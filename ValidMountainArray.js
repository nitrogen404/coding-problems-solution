var validMountainArray = function(arr) {
     let ans = false;
     var maxIndex = 0;
     if (arr.length > 2) {
     	for (let i = 0; i < arr.length - 1; i++) {
     		if (arr[i] < arr[i + 1]) {
     			maxIndex = i + 1;
     		}
     		else {
     			break;
     		}
     	}
     	if (maxIndex === 0 || maxIndex === arr.length - 1) {
     		return ans;
     	} 
     	else {
     		for (let j = maxIndex; j < arr.length - 1; j++) {
     			if (arr[j + 1] < arr[j]) {
     				ans = true;
     			}
     			else {
     				ans = false
     				break;
     			}
     		}
     	}
     	return ans;
     }
     else {
     	return ans;
     } 
};

console.log(validMountainArray([1, 3, 2]));