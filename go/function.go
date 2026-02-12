package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

// When two or more consecutive parameters share the same type we can emit all the types 
// except the last one 
func add_shorted_params(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 12))
	fmt.Println(add_shorted_params(42, 12))
}