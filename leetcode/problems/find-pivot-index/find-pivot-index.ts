/**
 * find pivot index
 * <right sum> = <sum of array> - <left sum> - <current elm in iteration>
 */
function pivotIndex(nums: number[]): number {
  const sum = nums.reduce((x, i) => x + i);
  let lSum = 0;

  for (let i = 0; i < nums.length; i++) {
    if (lSum === sum - lSum - nums[i])
      return i;
    lSum += nums[i];
  }

  return -1;
}

/**
 * test data
 */
interface testData {
  cases: number[][];
  expectedOutputs: number[];
}

const tests: testData = {
  cases: [
    [1, 7, 3, 6, 5, 6],
    [1, 2, 3],
    [2, 1, -1]
  ],
  expectedOutputs: [
    3,
    -1,
    0
  ]
};

/**
 * run test
 */
let output = null;
let expected = null;
for (let i = 0; i < tests.cases.length; i++) {
  output = pivotIndex(tests.cases[i]);
  expected = tests.expectedOutputs[i];

  if (output === expected)
    console.log('OK\n');
  else {
    console.log(`expectedOutput: ${expected}\noutput:${output}\n`);
  }
}
