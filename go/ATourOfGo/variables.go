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
// If we initialize the value go will infer the type of the variable
var y, z = 3, 4
// If we initialize we can also assign different types to the variables
var test1, test2 = 1, "hello"

// short variable declaration
// Inside a function we can declare and initialize a variable with the short variable declaration syntax
// Outside a function we cannot use the short variable declaration syntax so we have to use the var keyword
func return_k() int {
	k := 10
	return k
}
// k:=5 -> This will fail

func main() {
	var i int
	fmt.Println(i, c, python, java)
	fmt.Println(a, b, d)
	fmt.Println(i, j) // prints 0 2 why? because we reinitialize i in the main function
	fmt.Println(y, z) // prints 3 4 why? because we initialize y and z in the main function
	fmt.Println(test1, test2) // prints 1 hello why? because we initialize test1 and test2 in the main function
	fmt.Println(return_k()) // prints 10 why? because we return k from the return_k function
}