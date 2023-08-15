package main

import (
	"fmt"
)

func linear_search(haystack []int, needle int) bool {
	for i := 0; i < len(haystack); i++ {
		if haystack[i] == needle {
			return true
		}
	}

	return false
}

func main() {
	list := []int{1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420}
	target := 69 // true
	// target := 1336 // false
	// target := 69420 //true
	// target := 69421 // false
	// target := 1 // true
	// target := 0 // false

	res := linear_search(list, target)
	fmt.Println(res)
}
