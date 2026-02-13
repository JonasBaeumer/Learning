package main

import (
	"fmt"
	"runtime"
)

// Switch evaluation in go are exlusive meaning that we will only evaluate the block and and not the ones after it if its true so we dont need to 
// add any break statements
func main() {
	fmt.Println("Go runs on")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("macOS.")
	
	// Go will automatically check for duplicate cases so this will not compile
	//case "darwin":
	//	fmt.Println("THIS BLOCK WILL NOT EXECUTE")
	case "linux":
		fmt.Println("Linux.")
	default:
		fmt.Printf("%s.\n", os)
	}

	// Go evalates expression top to bottom meaning that all subsequents will not be looked and and therefore executed even if true
	i := 1
	// A switch without a condition is seen as Switch TRUE this is used to evaluate conditions 
	// If you assign a value the cases will be mapped against the value
	switch {
	case i < 0:
		fmt.Println("This is false")
	case i < 1:
		fmt.Println("This is false")
	case i < 2:
		fmt.Println("This is True")
	case i < 3:
		fmt.Println("This is also True but will not be evaluted in Go")
	}
}