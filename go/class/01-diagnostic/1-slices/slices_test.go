package slices

import (
	"reflect"
	"testing"
)

func TestGroupByLength(t *testing.T) {
	tests := []struct {
		name string
		in   []string
		want map[int][]string
	}{
		{"empty", nil, map[int][]string{}},
		{"one group", []string{"go", "is"}, map[int][]string{2: {"go", "is"}}},
		{"keeps order", []string{"fun", "go", "for", "is", "a"},
			map[int][]string{1: {"a"}, 2: {"go", "is"}, 3: {"fun", "for"}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := GroupByLength(tt.in)
			if got == nil {
				t.Fatal("got nil map, want empty map")
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("got %v, want %v", got, tt.want)
			}
		})
	}
}
