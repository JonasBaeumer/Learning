package main

import "fmt"

// A defer statement is a really powerful tool to make sure that we do some things later that we "shouldnt" forget
// With defer, we defer the execution of a statement until the sourrounding function returns
// The deferred calls arguments are evaluated imediately but the function call is not executed until the sourrounding function return 
// We can use this for example to handle behavior in case something crashes, for example to close the database connection

func main() {
	defer fmt.Println("Dont forget to close the database connection")
	fmt.Println("Doing something")
}