# 01 Diagnostic

Five small tasks, one per topic. Do them in order, as many as fit.
Each file has stubs that `panic("TODO")`. Replace the bodies.

| # | File | Topic | Run |
|---|---|---|---|
| 1 | `1-slices/slices.go` | slices and maps | `go test ./1-slices` |
| 2 | `2-stack/stack.go` | structs and methods | `go test ./2-stack` |
| 3 | `3-shapes/shapes.go` | interfaces | `go test ./3-shapes` |
| 4 | `4-age/age.go` | errors | `go test ./4-age` |
| 5 | `5-sum/sum.go` | goroutines and channels | `go test -race ./5-sum` |

## 1. GroupByLength
Group words by their length. Keep the input order inside each group.
`["go", "is", "fun"]` -> `{2: ["go", "is"], 3: ["fun"]}`.
An empty input returns an empty (non-nil) map.

## 2. Stack
An integer stack. `Push` adds on top, `Pop` removes and returns the top.
`Pop` on an empty stack returns `0, false`. The zero value `Stack{}` must
be ready to use.

## 3. TotalArea
Define a `Shape` interface with `Area() float64`. Make `Rect` and `Circle`
satisfy it. `TotalArea` sums any number of shapes.

## 4. ParseAge
Parse a string into an age.
- empty string: return `ErrEmpty`
- not a number: return an error that wraps the `strconv` error
  (so `errors.As(err, &numErr)` with `*strconv.NumError` works)
- negative or above 150: return `*RangeError` holding the value
- otherwise the age and `nil`

## 5. SumParallel
Split `nums` into `parts` chunks, sum each chunk in its own goroutine,
send the partial sums over a channel, and add them up. Must pass with
`-race`. `parts` is at least 1; it can be larger than `len(nums)`.
