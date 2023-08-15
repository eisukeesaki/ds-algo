package main

import (
	"fmt"
)

func sum_sequence(end int) int {
	if end == 1 {
		return 1
	}

	return end + sum_sequence(end-1)
}

func main() {
	end := 5
	sum := sum_sequence(end)
	fmt.Println("sum:", sum)
}
