package slices

// GroupByLength groups words by length, keeping input order within a group.
func GroupByLength(words []string) map[int][]string {
	m := map[int][]string{}
	for _, word := range words {
		m[len(word)] = append(m[len(word)], word)
	}
	return m
}
