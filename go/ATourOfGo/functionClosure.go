// Go functions may be closure
// closure -> A function value that references variables from outside the body 
// the function may access and assign to the referenced variables
// You could say the function is "bound" to the variables 

package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}