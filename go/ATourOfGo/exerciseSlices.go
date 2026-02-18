// Should return a slice of length dy, each element is a slice of dx 8-bit unsinged int
// When running the program will display your picture, interpreting integers as grayscale

// Implement different functions to draw different images

// Need to use a loop to allocate each []uint9 inside the [][]uint8

// Use iunt(intValue) to convert between types

// What is the size of a uint8? -> One byte (e.g. 8 bit)
// a slice of that can have variable length

package main

import (
	"fmt"
	"golang.org/x/tour/pic"
)

func functionOne(x, y int) uint8{
	return uint8((x+y)/2)
}

func Pic(dx, dy int) [][]uint8 {
	pic := make([][]uint8, dy)
	// Initialize the individual uint arrays 
	// dy uint8 slizes, each of length dx
	fmt.Println(pic)
	// Initialize and add all the inner slices of size dx
	for i := 0; i < dy; i++ {
		// Need to make a slice here instead of an array, since for arrays we must know the size at compile time!
		// It has to be a fixed number and cant be a variable
		inner := make([]uint8, dx) 

		for j := 0; j < dx; j++ {
			inner[j] = functionOne(i, j)
		}
		// Creat the inner array and then will it with values according to the function
		pic[i] = inner
	}

	fmt.Println(pic) 


	return pic
}

func main() {
	pic.Show(Pic)
}
