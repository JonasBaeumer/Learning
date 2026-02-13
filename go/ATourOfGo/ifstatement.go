package main 

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

// We can also declare if statements with local variables and short statement to run for the execution in the scope only and evaluation blocks
func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v 
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	// However this is outside the eval block now so we could not use v
	return lim
}

// Variables declared inside the if statement are not only available in the if block but also all of the else condition blocks


func main() {
	fmt.Println(sqrt(9), sqrt(-1), sqrt(22.22))
	fmt.Println(
		pow(3, 2 , 10),
		pow(3, 3, 10),
	)
}
