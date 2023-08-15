package main

import (
	"fmt"
)

func bubble_sort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for k := 0; k < len(arr)-1-i; k++ {
			if arr[k] > arr[k+1] {
				tmp := arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = tmp
			}
		}
	}
	return arr
}

func main() {
	list := []int{2, 5, 1, 4, 3, 5, -42, 42}
	sorted := bubble_sort(list)
	fmt.Println(sorted)
}
