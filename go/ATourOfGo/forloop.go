package main

import "fmt"

func main() {
	
	// The traditional for loop, and in go there is only this one type of for loop
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i 
	}
	fmt.Println(sum)

	// Here we can use the normal variable declaration syntax as well
	var total int = 1
	// However we cannot use the short variable declaration syntax in the loop or otherwise it will fail to compile
	// for var i int = 0; i < 10; i++ { -> PRODUCES AN ERROR BECAUSE var and int are both not allowed in the loop
	for i := 0; i < 10; i++ {
		total += i
	}
	fmt.Println(total)
}

