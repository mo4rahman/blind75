// function containsDuplicate(array) {
//   const comparisonObject = {};

//   for (let i = 0; i < array.length; i++) {
//     if (array[i] in comparisonObject) {
//       // Duplciate
//       return true;
//     } else {
//       comparisonObject[array[i]] = 1;
//     }
//   }
//   return false;
// }

function containsDuplicate(array) {
  const comparisonSet = new Set(array);
  // console.log(comparisonSet);
  // console.log(comparisonSet.size)
  if (comparisonSet.size === array.length) {
    return false;
  } else {
    return true;
  }
}

console.log(containsDuplicate([1, 2, 3, 4])); // False
console.log(containsDuplicate([1, 2, 3, 4, 1])); // True
