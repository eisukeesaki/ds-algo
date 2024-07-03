"use strict";
function getRunningSum(nums) {
    let sum = 0;
    return nums.map(element => sum += element);
}
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
const input = [3, 1, 2, 10, 1];
const runningSum = getRunningSum(input);
console.log(runningSum);
