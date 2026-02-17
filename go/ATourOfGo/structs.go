// A struct is a collection of fields and is probably the thing the most closely resembles OOO programming

package main

import "fmt"

type Vertex struct {
	X, Y int  
}

var ( // This is a struct literal
	v1 = Vertex{1, 2} // this is type vertex
	v2 = Vertex{X: 1} // Y default initialized to 0
	v3 = Vertex{} // 0,0 default
	p = &Vertex{1, 2} // type *Vertex
)

func main() {
	test := Vertex{1, 2}

	fmt.Println(test)

	// We can access the individual field of a struct using normal . (like in other OOO languages)
	fmt.Println(test.X)
	fmt.Println(test.Y)

	// Struct field can also be accessed by struct pointers
	pointer := &test
	fmt.Println(pointer.X) // We have to use this notation here so that we can properly reference the pointer 
	//fmt.Println(*pointer.X) // invalid operation: cannot indirect pointer.X (variable of type int)

	fmt.Println(v1, p, v2, v3)
}