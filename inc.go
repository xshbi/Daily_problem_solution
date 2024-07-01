
/*Given an integer n, return a counter function. This counter function initially returns n and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).*/




package main

import "fmt"

func createCounter(n int) func() int {
    count := n
    return func() int {
        count++
        return count - 1
    }
}

func main() {
    counter := createCounter(10)
    fmt.Println(counter()) // Output: 10
    fmt.Println(counter()) // Output: 11
    fmt.Println(counter()) // Output: 12
    fmt.Println(counter()) // Output: 13
}


/*
Output:
10
11
12
13
*/
