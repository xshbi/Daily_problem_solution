package main

import "fmt"

// Function to calculate the sum of the interior angles of a polygon
func sumOfAngles(n int) int {
    if n < 3 {
        fmt.Println("A polygon must have at least 3 sides.")
        return 0
    }
    return (n - 2) * 180
}

func main() {
    sides := 5 // For a pentagon
    fmt.Printf("The sum of the interior angles of a polygon with %d sides is %d degrees.\n", sides, sumOfAngles(sides))
}
