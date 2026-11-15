package stack

// Stack is a LIFO stack of ints. The zero value is an empty stack.
type Stack struct {
	stack []int
}

func (s *Stack) Push(v int) {
	s.stack = append(s.stack, v)
}

func (s *Stack) Pop() (int, bool) {
	stackLength := s.Len()
	if stackLength == 0 {
		return 0, false
	}
	value := s.stack[stackLength-1]
	s.stack = s.stack[:stackLength-1]
	return value, true
}

func (s *Stack) Len() int {
	return len(s.stack)
}
