package sum

import "testing"

func TestSumParallel(t *testing.T) {
	nums := make([]int, 1000)
	want := 0
	for i := range nums {
		nums[i] = i
		want += i
	}
	for _, parts := range []int{1, 3, 7, 1000, 2000} {
		if got := SumParallel(nums, parts); got != want {
			t.Errorf("parts=%d: got %d, want %d", parts, got, want)
		}
	}
	if got := SumParallel(nil, 4); got != 0 {
		t.Errorf("empty: got %d, want 0", got)
	}
}
