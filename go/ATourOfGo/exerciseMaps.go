// Implement WordCount. It should return a map of the counts of each “word” in the string s. 
// The wc.Test function runs a test suite against the provided function and prints success or failure.

// You might find strings.Fields helpful.

package main

import (
	"fmt"
	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	wordCount := make(map[string]int)
	for i := 0; i < len(s); i++ {
		if _, ok := wordCount[string(s[i])]; ok {
			wordCount[string(s[i])] += 1
		} else {
	 	 	wordCount[string(s[i])] = 1
		}
	}

	// Other way to write the for loop
	for _, r in range s {
		if _, ok := wordCount[string(s[r])]; ok {
			wordCount[string(s[r])] += 1
		} else {
	 	 	wordCount[string(s[r])] = 1
		}
	}


	fmt.Println(wordCount)
	return wordCount
}

func main() {
	wc.Test(WordCount)
}