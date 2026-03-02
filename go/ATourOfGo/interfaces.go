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
}