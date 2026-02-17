package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {
	var z float64 = 1
	var prevz float64 = z

	for i := 0; i < 10; i++ {
		z -= (z*z - x) / (2*z)
		fmt.Println(fmt.Sprint(z))
		if z == prevz {
			return z
		} else {
			prevz = z 
		}
	}
	return z
}

func main() {
	fmt.Println("Test")
	var testValue float64 = 27
	fmt.Println("The final value is" + fmt.Sprint(Sqrt(testValue)))
}