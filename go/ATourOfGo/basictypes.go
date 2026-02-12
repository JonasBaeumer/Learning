package main

import (
	"fmt"
	"math/cmplx"
)
// These are the following basic types in go:
// bool
// string
// int  int8  int16  int32  int64
// uint uint8 uint16 uint32 uint64 uintptr
// byte // alias for uint8
// rune // alias for int32
// float32 float64
//complex64 complex128

// We can also declare variables in blocks as with import statements
var (
	ToBe bool = false
	MaxInt uint64 = 1<<64 - 1
	z complex128 = cmplx.Sqrt(-5 + 12i)
)

// Variables declared without a value are initialized with their zero value
// bool -> false
// int -> 0
// string -> ""
// float -> 0.0
// complex -> 0.0i
// byte -> 0
// rune -> 0
// uint -> 0
// uintptr -> 0

// We can also convert types with the type conversion syntax T(v)
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)

// constants are declared like variables but with the const keyword
const Pi = 3.14
const pi float64 = 3.14
// For constants the short variable declaration syntax is NOT allowed
// const pi = 3.14 -> This will fail

func main() {
    // Also works inside a function!
	var (
		ToBe bool = false
		MaxInt uint64 = 1<<64 - 1
		z complex128 = cmplx.Sqrt(-5 + 12i)
	)
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
	
	fmt.Println(f, u)

	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)

	fmt.Println(Pi, pi)
}