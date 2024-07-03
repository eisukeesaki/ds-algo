package main

import "fmt"

type Node struct {
	Value int
	Left  *Node
	Right *Node
}

func insert(root *Node, value int) *Node {
	if root == nil {
		return &Node{Value: value}
	}
	if value < root.Value {
		root.Left = insert(root.Left, value)
	} else {
		root.Right = insert(root.Right, value)
	}
	return root
}

func printInOrder(root *Node) {
	if root != nil {
		printInOrder(root.Left)
		fmt.Println(root.Value)
		printInOrder(root.Right)
	}
}

func main() {
	var root *Node
	values := []int{10, 6, 15, 3, 8, 20}
	for _, v := range values {
		root = insert(root, v)
	}
	printInOrder(root)
}
