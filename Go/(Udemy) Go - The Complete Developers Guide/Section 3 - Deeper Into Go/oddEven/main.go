package main

import "fmt"

func main() {
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	for _, value := range nums {
		if value%2 == 0 {
			fmt.Printf("%d is even", value)

		} else {
			fmt.Printf("%d is odd", value)
		}
		fmt.Println()
	}
}
