package main

import (
	"fmt"
	"math"
)

func find_breakpoint(building []bool) int {
	if building[0] {
		return 0
	}

	step := int(math.Sqrt(float64(len(building))))
	for i := step; i < len(building); i += step {
		if building[i] { // breakage of the first ball tells you: you went too high
			safepoint := i - step
			for i := safepoint; i < len(building); i++ {
				if building[i] { // second ball breaks, and here is the breakpoint
					return i
				}
			}
		}
	}

	return -1
}

func main() {
	// the ball would break if dropped from true-th floor
	// 16 = len(building)
	// 11 = breakpoint
	building := []bool{false, false, false, false, false, false, false, false, false, false, false, true, true, true, true, true}
	// building := []bool{true} // breakpoint = 0
	// building := []bool{false}

	res := find_breakpoint(building)
	fmt.Println("breakpoint is", res)
}
