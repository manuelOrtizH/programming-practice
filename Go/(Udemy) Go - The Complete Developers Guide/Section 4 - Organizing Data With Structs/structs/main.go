package main

import (
	"fmt"
)

type person struct {
	firstName string
	lastName  string
	contactInfo
}

type contactInfo struct {
	email string
	zip   int
}

func main() {
	manuel := person{
		firstName: "Manuel",
		lastName:  "Ortiz",
		contactInfo: contactInfo{
			email: "manuoh09@gmail.com",
			zip:   38100,
		},
	}

	manuel.updateName("Enriqueto")
	manuel.print()

	mySlice := []string{"Hi", "There", "How", "Are", "You"}
	updateSlice(mySlice)

	name := "Anacleto"
	namePointer := &name
	fmt.Println(&namePointer)
	printPointer(namePointer)
}

func printPointer(namePointer *string) {
	fmt.Println(&namePointer)
}

func updateSlice(s []string) {
	s[0] = "Hello"
}

func (p person) print() {
	fmt.Printf("%+v", p)
	fmt.Println()
}

func (pointerToPerson *person) updateName(newName string) {
	(*pointerToPerson).firstName = newName
}
