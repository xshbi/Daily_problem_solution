package main

import "fmt"

// ListNode represents a node in the linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// FindMiddle finds the middle element of the linked list.
func FindMiddle(head *ListNode) *ListNode {
	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	return slow
}

func main() {
	// Example usage
	list := &ListNode{Val: 1}
	list.Next = &ListNode{Val: 2}
	list.Next.Next = &ListNode{Val: 3}
	list.Next.Next.Next = &ListNode{Val: 4}
	list.Next.Next.Next.Next = &ListNode{Val: 5}

	middle := FindMiddle(list)
	fmt.Printf("Middle element: %d\n", middle.Val)
}
