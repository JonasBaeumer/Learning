package main

import "fmt"

var a[10] int // default initialized with 0s
var b[2] string

// Arrays are fixed size and can not be changed, however there is a way to work around that: Slices
// A slice is a dynamically-sized, flexible view into the element of an array
// Slices in practice are much more common than arrays
// A slice does not store any actual data it just points towards a section of an underlying array

func main() {
	fmt.Println(a)
	
	b[0] = "Hello"
	b[1] = "World"

	fmt.Println(b)

	// A slide can be defined by providing the index bound low, high
	// It will include the lower bound index, but will exclude the higher bound index so [low, high)

	primes := [6]int{2,3,5,7,11,13}
	slice_prime := primes[1:4]
	fmt.Println(slice_prime)

	// If you change the underlying array the slices will also be changed
	slice_prime[1] = 100 // You can change the array through the slice, be careful though that the index you adress in the slice
	// is relative to the window, e.g. in this example slice[1] is the second value in the slice! not the underlying index 1
	// which would be the actual first value of the interval
	primes[1] = 1000
	fmt.Println(slice_prime)

	// A slice literal is like an array literal without the length 
	// Under the hood it builds an array and then builds a slice that references it
	q := []int{2,3,5,7,11,13}
	fmt.Println(q)

	// This is an array literal
	p := [6]int{2,3,5,7,11,13}
	fmt.Println(p)

	// This is an anonymous struct slice
	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)

	// When using slices the high and low bounds have default values
	// low by default is 0
	// high by default is max_length
	fmt.Println(p[:6])
	fmt.Println(p[0:])
	fmt.Println(p[:])

	// For slice we can access two important attributes:
	// Its length -> The number of elements it contains
	// The capacity -> The number of elements in the underlying array (counting from the first element in the slice)
	fmt.Printf("len=%d cap=%d %v\n", len(p[1:4]), cap(p[1:4]), s[1:4])
	fmt.Printf("len=%d cap=%d %v\n", len(p[1:4]), cap(p[0:4]), s[1:4])

	// The zero value of a slice is nil, with a capity and length of 0
	var emptyslice []int
	fmt.Printf("len=%d cap=%d %v\n", len(emptyslice), cap(emptyslice), emptyslice)
}