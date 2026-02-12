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

func swap(x, y string) (string, string) {
	return y, x
}

// Naked returns: We may name the return values in the function header, if we just return at the end the named return 
// values will be returned 
// That means the methods are automatically defined during default initialization
func split(sum int) (x, y string) {
	return
}

func main() {
	fmt.Println(add(42, 12))
	fmt.Println(add_shorted_params(42, 12))
	fmt.Println(swap("hello", "world"))
	fmt.Println(split(10))
}