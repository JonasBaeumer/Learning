package stack

import "testing"

func TestStack(t *testing.T) {
	var s Stack
	if _, ok := s.Pop(); ok {
		t.Fatal("Pop on empty stack: ok = true")
	}
	s.Push(1)
	s.Push(2)
	s.Push(3)
	if s.Len() != 3 {
		t.Fatalf("Len = %d, want 3", s.Len())
	}
	for _, want := range []int{3, 2, 1} {
		got, ok := s.Pop()
		if !ok || got != want {
			t.Fatalf("Pop = %d, %v; want %d, true", got, ok, want)
		}
	}
	if s.Len() != 0 {
		t.Fatalf("Len = %d after popping all, want 0", s.Len())
	}
}
