package main

import "fmt"

// Function to calculate the maximum edge of a triangle
func maxEdge(side1, side2 int) int {
    return (side1 + side2) - 1
}

func main() {
    // Example usage
    side1 := 8
    side2 := 10
    fmt.Printf("The maximum edge of the triangle with sides %d and %d is %d\n", side1, side2, maxEdge(side1, side2))
}
