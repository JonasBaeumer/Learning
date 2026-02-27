// Go does have standalone methods, it only has functions

// However we can define functions with receiver arguments to effectively work like a method

package main 

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func Abs(v Vertex) float64 {
	return math.Sqrt(v.X * v.X + v.Y * v.Y)
}

// We can also declare methods on non-struct types
// However we need to be careful with defining those types in the samage package as the methods,
// We can not declare them somewhere else

// Why do we even declare a type this way? Because we want to add methods to it! In go we can not 
// add methods to default types such as float64 so we need to use the type wrapper
type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	} else {
		return float64(f)
	}
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(Abs(v))

	var myFloat MyFloat = -64
	fmt.Println(myFloat.Abs())
}