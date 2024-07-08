package main

import "fmt"

// Function to find the product of digits of a number
func productOfDigits(N int) int {
    // Stores the product of digits of a number
    product := 1

    for N != 0 {
        product *= N % 10
        N /= 10
    }

    // Return the product
    return product
}

// Function to print all numbers upto N having product of digits equal to K
func productOfDigitsK(N, K int) {
    // Stores whether any number satisfying the given conditions exists or not
    flag := 0

    // Iterate over the range [1, N]
    for i := 1; i <= N; i++ {
        // If product of digits of i is equal to K or not
        if K == productOfDigits(i) {
            fmt.Print(i, " ")
            flag = 1
        }
    }

    // If no numbers are found
    if flag == 0 {
        fmt.Println("-1")
    }
}

func main() {
    // Given value of N & K
    N, K := 500, 10

    // Function call to print all numbers from [1, N] with product of digits K
    productOfDigitsK(N, K)
}
