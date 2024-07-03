function twoSum(nums: number[], target: number): number[] {
  const numsMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const diff = target - num;

    if (numsMap.has(diff))
      return [numsMap.get(diff), i];

    numsMap.set(num, i);
  }
}

// expected output: [0, 1]
// const numbers = [2, 7, 11, 15];
// const target = 9;

// expected output: [1,2]
// const numbers = [3, 2, 4];
// const target = 6;

// expected output: [0,1]
// const numbers = [3, 3];
// const target = 6;

const numbers = [5, 9, 4, 2, 0, 6, 7, 1, 10, 8];
const target = 6;

console.log(`numbers: ${numbers}`);
console.log(`target: ${target}`);

const indices = twoSum(numbers, target);

console.log(indices);

