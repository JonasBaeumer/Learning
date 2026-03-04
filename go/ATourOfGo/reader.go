package main

import (
	"fmt"
	"strings"
	"io"
)

// The reader interface gives you a standard interface which is implemented across many data sources in go to 
// consecutively read in data without having to read in the whole file/source in memory 
// Why this matters
// The power is that any source can implement this interface. Your code that reads from a strings.Reader works identically with:
// - a file (os.File)
// - an HTTP response body (http.Response.Body)
//  - a gzip stream (gzip.Reader)
//  - ...anything

  You never change your reading logic — just swap the source.

func main() {
	r := strings.NewReader("Hello, Reader!")  // source: a string

  	buf := make([]byte, 8)  // your buffer, 8 bytes wide

  	for {
      n, err := r.Read(buf)
      fmt.Printf("n=%d buf=%q\n", n, buf[:n])
      if err == io.EOF {
          break
      }
  }
}