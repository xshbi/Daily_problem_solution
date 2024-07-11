package main

import "fmt"

func reverseString(s string) string {
    result := ""
    for _, c := range s {
        result = string(c) + result
    }
    return result
}

func main() {
    original := "Hello, World!"
    reversed := reverseString(original)
    fmt.Println("Original:", original)
    fmt.Println("Reversed:", reversed)
}
