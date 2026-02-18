package main

import "fmt"

// A map has the default value nil
// A nil map has no keys, nor can keys be added 
// The make function returns a map of a given type which is initialized and ready for use

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

// Map are like struct literals but the keys are required 
var maps = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

// If the top level is just a type name it can be ommited the type will be inferenced by go
var maps_ommited = map[string]Vertex{
	"Datadog": {12312, 123123},
}

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
	fmt.Println(maps["Google"])
	fmt.Println(maps_ommited["Datadog"])

	m := make(map[string]int)
	// The basic operations we can do on a map are: Insert/Update, retrieve, delete, check if key is present, 
	// Insert
	m["Hi"] = 42
	fmt.Println(m["Hi"])

	// Retrieve
	val := m["Hi"]
	fmt.Println(val)

	// delete
	delete(m, "Hi")
	fmt.Println(m)

	// Check if value is present
	m["Hi"] = 40
	v, ok := m["Hi"]
	fmt.Println("The value:", v, "Present?", ok)
	v, ok = m["Datadog"]
	fmt.Println("The value:", v, "Present?", ok)
}