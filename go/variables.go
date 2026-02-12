package main

import "fmt"

// var declares a list of variables
// as in function declaration is they share the same type keyword we can do it last
var c, python, java bool
// all element in the list must share the same type or the code will fail to compile
// var c, python, java bool swift int -> WILL NOT WORK
var a, b, d int

func main() {
	var i int
	fmt.Println(i, c, python, java)
	fmt.Println(a, b, d)
}