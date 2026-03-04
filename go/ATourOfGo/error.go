package main

import (
	"fmt"
	"strconv"
)

func Sqrt(x float64) (float64, error) {
	return 0, nil
}

func main() {

	// Go functions express an error state with the error variable 
	// Therefore code should test for errors while by testing wether the error equals nil

	i, err := strconv.Atoi("42")

	if err != nil {
		fmt.Printf("couldn't convert number: %v\n", err)
    	return
	}
	
	fmt.Println("Converted integer:", i)

	j, err := strconv.Atoi("HelloIamWorld")

	if err != nil {
		fmt.Printf("couldn't convert number: %v\n", err)
    	return
	}

	fmt.Println("Converted integer:", j)

	nbr, err := Sqrt(-2)

	if err != nil {
		fmt.Printf("Couldn't draw square root from number: %v\n", err)
		return
	}

	fmt.Println("Square root:", nbr)
}