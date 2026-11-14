package shapes

import (
	"math"
	"testing"
)

func TestTotalArea(t *testing.T) {
	var _ Shape = Rect{}
	var _ Shape = Circle{}

	if got := TotalArea(); got != 0 {
		t.Errorf("TotalArea() = %v, want 0", got)
	}
	got := TotalArea(Rect{W: 2, H: 3}, Circle{R: 1})
	want := 6 + math.Pi
	if math.Abs(got-want) > 1e-9 {
		t.Errorf("TotalArea = %v, want %v", got, want)
	}
	shapes := []Shape{Rect{W: 1, H: 1}, Rect{W: 2, H: 2}}
	if got := TotalArea(shapes...); got != 5 {
		t.Errorf("TotalArea(shapes...) = %v, want 5", got)
	}
}
