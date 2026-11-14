package age

import (
	"errors"
	"strconv"
	"testing"
)

func TestParseAge(t *testing.T) {
	if got, err := ParseAge("42"); err != nil || got != 42 {
		t.Errorf("ParseAge(42) = %d, %v; want 42, nil", got, err)
	}
	if _, err := ParseAge(""); !errors.Is(err, ErrEmpty) {
		t.Errorf("ParseAge(\"\") err = %v, want ErrEmpty", err)
	}
	_, err := ParseAge("abc")
	var numErr *strconv.NumError
	if !errors.As(err, &numErr) {
		t.Errorf("ParseAge(abc) err = %v, want it to wrap *strconv.NumError", err)
	}
	for _, s := range []string{"-1", "151"} {
		_, err := ParseAge(s)
		var rangeErr *RangeError
		if !errors.As(err, &rangeErr) {
			t.Errorf("ParseAge(%s) err = %v, want *RangeError", s, err)
			continue
		}
		if want, _ := strconv.Atoi(s); rangeErr.Age != want {
			t.Errorf("RangeError.Age = %d, want %d", rangeErr.Age, want)
		}
		if rangeErr.Error() == "" {
			t.Error("RangeError.Error() is empty")
		}
	}
}
