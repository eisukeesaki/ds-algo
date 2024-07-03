function isDoubledArray(arr) {
  if (arr.length % 2 === 0) {
    let iC = (arr.length - 1) / 2;
    for (let iO = 0; arr.length; iO++) {
      if (arr[iO] != arr[iC] / 2) {
        return false;
      }
    }
    return true;
  } else {
    return false;
  }
}

function findOriginalArray(changed) {
  if (isDoubledArray(changed))
    console.log("now, let's find the original array");
  else
    return [];
}

function main() {
  let changed = [1, 3, 4, 2, 6, 8];

  const original = findOriginalArray(changed);

  console.log("original: %o", original);
}

main();
