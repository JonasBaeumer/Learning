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

	// However the initialization and post statements are optional, so the following is also possible
	sum = 0
	for ; sum < 100; {
		sum += 1
	}
	fmt.Println(sum)

	// While we dont have a normal while loop we can write a for loop the same way
	x := 1
	for x < 100 {
		x += 10
	}
	fmt.Println(x)

}

