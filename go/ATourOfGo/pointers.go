// A pointer holds the memory adress of a value
// a pointer has the zero value nil
// & generates a pointer to its operand (like in c++)
// * denotes the pointers underlying value

package main

import "fmt"

func main() {
	i := 42
	p := &i 

	// We can read out the pointer directly
	fmt.Println(p)
	// We can also read out the value the pointer is pointed towards
	fmt.Println(*p)

	// However we can also directly set I through the pointer (dereferencing / indirecting)
	*p = 21
	fmt.Println(i)


}