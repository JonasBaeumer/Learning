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

func (c BigCat) Sound() string {
	return "Miauwwwww!"
}

func main() {
	var charlie = BigCat{80, "Kitten"}
	fmt.Println(charlie.Sound())
}