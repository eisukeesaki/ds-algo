package main

import (
	"fmt"
)

func bs_list(haystack []int, needle int) bool {
	lo := 0
	hi := len(haystack)

	for lo < hi {
		mid := lo + (hi-lo)/2
		v := haystack[mid]

		if v == needle {
			return true
		} else if v > needle {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return false
}

func main() {
	list := []int{1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420}
	target := 69 // true
	// target := 1336 // false
	// target := 69420 // true
	// target := 69421 // false
	// target := 1 // true
	// target := 0 // false

	res := bs_list(list, target)
	fmt.Println(res)
}
