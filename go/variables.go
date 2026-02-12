package main

import "fmt"

// var declares a list of variables
// as in function declaration is they share the same type keyword we can do it last
var c, python, java bool
// all element in the list must share the same type or the code will fail to compile
// var c, python, java bool swift int -> WILL NOT WORK
var a, b, d int

// Variables with initializers
var i, j int = 1, 2
var y, z = 3, 4

func main() {
	var i int
	fmt.Println(i, c, python, java)
	fmt.Println(a, b, d)
	fmt.Println(i, j) // prints 0 2 why? because we reinitialize i in the main function
	fmt.Println(y, z) // prints 3 4 why? because we initialize y and z in the main function
}