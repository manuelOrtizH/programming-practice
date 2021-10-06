/*
    Destructuring Arrays
*/
const alphabet = ['A', 'B', 'C', 'D', 'E', 'F'] 
const numbers = ['1', '2', '3', '4', '5', '6'] 
const [a,, c, ...rest] = alphabet


//Combine two arrays together
const newArray = [... alphabet, ...numbers]

function sumAndMultiply(a,b){
    return [a+b, a*b, a/b]
}

const [sum, multiply, division = 'No division'] = sumAndMultiply(2,3)

/*
    Destructuring Objects
*/

/*const personOne = {
    name: 'Pingu',
    age: 8,
    favoriteFood: 'Salmón',
    address: {
        country: 'Polo Sur',
        city: 'Fríolandia'
    }
}

const personTwo = {
    name: 'Perrito',
    age: 40,
    address:{
        country: 'Japón',
        city: 'Hong Kong'
    }
}

const { name: firstName = 'Cotorrito', age, favoriteFood = 'Default Rice' } = personOne
console.log(firstName)
console.log(age)
console.log(favoriteFood)*/

/*const {age, ...restante} = personTwo
console.log(restante)*/

/*const {name: firstName, address: { country }} = personTwo
console.log(firstName)
console.log(city)*/

//Combine different objects
const personOne = {
    name: 'Pingu',
    age: 8,
    favoriteFood: 'Salmón',
    address: {
        country: 'Polo Sur',
        city: 'Fríolandia'
    }
}

const personTwo = {
    age: 40,
    favoriteFood: 'Croquetas'
}

const personThree = {...personOne, ...personTwo}
//console.log(personThree)

function printUser({ name, age, favoriteFood='Rice'}){
    console.log(`Name is:  ${name}. Age is: ${age}. Food is: ${favoriteFood}`)
}

printUser(personOne)


