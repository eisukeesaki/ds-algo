package main

import (
	"fmt"
)

func canBeIncreasing(nums []int) bool {
	cnt := 0
	for i := 1; i < len(nums) && cnt < 2; i++ {
		if nums[i-1] >= nums[i] {
			cnt++
			if i > 1 && nums[i-2] > nums[i] {
				nums[i] = nums[i-1]
			}
		}
	}
	return cnt < 2
}

func testSolution() {
	cases := [][]int{
		{1, 2, 10, 5, 7}, // true
		{2, 3, 1, 2},     // false
		{1, 1, 1},        // false
	}

	for _, c := range cases {
		fmt.Println("input:", c)
		res := canBeIncreasing(c)
		fmt.Println(res)
	}
}

func main() {
	testSolution()
}
