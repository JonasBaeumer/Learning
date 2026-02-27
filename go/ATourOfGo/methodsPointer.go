package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

// Methods can also have pointers as receivers, while that is the case we still modify the 
// the unerlying value it points towards

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f 
}

// What would now happen if we rewrite the Scale methods without * the pointer?
// Since we dont return the changed object actually nothing would change 
// That is when we dont call the pointer scale would receive a copy of the underlying v
// object, since we dont return a value and subsequently overwrite it the copy just 
// gets lost and therefore nothing changes
// func (v Vertex) Scale(f float64) {
//	v.X = v.X * f
//	v.Y = v.Y * f 
// }

func ScaleFunc(v *Vertex, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
// What would happen if we call a method with pointer receiver with a pointer and vice versa?
// var v Vertex
// ScaleFunc(v, 5)  // Compile error!
// ScaleFunc(&v, 5) // OK

// while methods with pointer receivers take either a value or a pointer as the receiver when they are called:
// var v Vertex
// v.Scale(5)  // OK
// p := &v
// p.Scale(10) // OK

// In General when there is function arguments the function arguments must always exactly match 
// the specifified type in the argument e.g. func(*T) must provide something of type *T, while 
// func(T) must provide type T

// So what are the reasons to use a pointer receiver?
// 1. You want to modify the underlying value
// 2. You want to avoid making copies on every method call (efficient for larger structs)


func main () {
	v := Vertex{3, 4}
	v.Scale(10)

	fmt.Println(v.Abs())
}