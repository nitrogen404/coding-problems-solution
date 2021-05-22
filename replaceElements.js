var replaceElements = function(arr) {
     let lastElement = arr[arr.length - 1];
     arr[arr.length - 1] = -1;

     let currentMax = lastElement;
     for (let i = arr.length - 2; i > -1; i--) {
          if (arr[i] < currentMax) {
               arr[i] = currentMax;
          }
          else {
               let temp = arr[i];
               arr[i] = currentMax;
               currentMax = temp;
          }
     }
     return arr;
};

console.log(replaceElements([17, 18, 5, 4, 6, 1]));