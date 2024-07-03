/**
 * fast & low memory usage
 */
// function getRunningSum(nums: number[]): number[] {
//   let runningSum = nums;

//   for (let i = 1; i < runningSum.length; i++) {
//     runningSum[i] = nums[i - 1] + nums[i];
//   }

//   return runningSum;
// }

/**
 * readable
 */
function getRunningSum(nums: number[]): number[] {
  const rSum = new Array(nums.length);

  rSum[0] = nums[0];

  for (let i = 1; i < rSum.length; i++) {
    rSum[i] = rSum[i - 1] + nums[i];
  }

  return rSum;
}

/**
 * clever
 */
// function getRunningSum(nums: number[]): number[] {
//   let sum: number = 0;

//   return nums.map(element => sum += element);
// }

/** expected input:output
 * input:  [1,2,3,4]
 * output: [1,3,6,10]
 */
// const input: Array<number> = [1,2,3,4];

/** expected input:output
 * input:  [1,1,1,1,1]
 * output: [1,2,3,4,5]
 */
// const input: Array<number> = [1,1,1,1,1];

/** expected input:output
 * input:  [3,1,2,10,1]
 * output: [3,4,6,16,17]
 */
const input: Array<number> = [3, 1, 2, 10, 1];

const runningSum: Array<number> = getRunningSum(input);

console.log(runningSum);
