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
// func (v *Vertex) Scale(f float64) {
//	v.X = v.X * f
//	v.Y = v.Y * f 
// }

func main () {
	v := Vertex{3, 4}
	v.Scale(10)

	fmt.Println(v.Abs())
}