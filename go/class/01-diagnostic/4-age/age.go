package age

// TODO: declare ErrEmpty (a sentinel error).

// RangeError reports an age outside 0..150.
type RangeError struct {
	Age int
}

// TODO: make *RangeError satisfy the error interface.

// ParseAge parses s as an age between 0 and 150.
func ParseAge(s string) (int, error) {
	panic("TODO")
}
