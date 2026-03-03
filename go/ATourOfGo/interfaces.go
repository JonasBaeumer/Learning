package main

import (
	"fmt"
)

type Cat interface {
	Sound() string
}

type BigCat struct {
	height int
	name string
}

type SmallCat struct {
	height int
	name string
}

func (c *BigCat) Sound() string {
	if c == nil {
		return "There is no cat :("
	}
	return "Miauwwwww!"
}

func (c SmallCat) Sound() string {
	return "Miauwuuuuuu!"
}

// Notice here that the interface is implemented implicitly, this is resolved at compile time
// if a type implements all the methods of the interface it automatically 
// satisfied the interface

func main() {
	// Nil pointer receiver demo — animal holds (nil, *BigCat), still non-nil interface
	var c *BigCat = nil
	var animal Cat = c
	fmt.Println(animal.Sound()) // "There is no cat :("

	// Under the hood interfaces can be thought of as a tuple of a value and a concrete type when they are assigned (value, type)
	// That makes interfaces very powerful as we can reassign it to every type that implements the required methods and it will work
	// Calling a method on an interface value executes the method of the same name on its underlying type.
	var charlie = &BigCat{80, "Kitten"} // pointer, matches *BigCat receiver
	var jet = SmallCat{25, "SmallKitten"}
	animal = charlie
	fmt.Println(animal.Sound()) // calls BigCat's Sound()
	animal = jet
	fmt.Println(animal.Sound()) // calls SmallCat's Sound()

	// We can also declare an empty interface which can then handle any arbitrary type 
	// This is usefull when handling unknown values 
	var i interface{}

	// Type assertions: when wrapped / declared in an interface we can not directly acess the underlying type 
	// That is problematic because we can not access function that would work on the original type but will throw an error 
	// for when being called on the interface 
	// Calling that will trigger a panic -> A runtime crash the programm stops executing, really bad!

	// Key role:
  	// Type assertions only work on interface types. You can't assert on a concrete type directly — there's nothing to unwrap.
	// You already know if the type is a string because that is induced at compile time or explicitly declared 
	// If like saying to the compiler, check if this string is a string - doesnt make sense

	var j interface{} := "Hello World"
	// j.ToUpper() -> j i an interface not a string! Will trigger a panic / crash (bad)

	// To check what the interface contains you can do a safe assertion
	// Essentially we are asking: "Give me the value if it exists, tell me if it does not"
	s, ok := j.(string)
	fmt.Println(j, ok)

	ints, ok := j.(int)
	fmt.Println(ints, ok) // Will return false, but wont crash because we safe assert

	// If we have multiple possible time, instead of chaining if statements together we can use SWITCH CASE 
	// which is much more elegant 
	
	switch v := j.(type) {
	case int:
		fmt.Printf("int: %d\n", v)
	case string:
		fmt.Printf("string: %q\n", v)
	default:
		fmt.Printf("unknown type: %T\n", v)
	}



}