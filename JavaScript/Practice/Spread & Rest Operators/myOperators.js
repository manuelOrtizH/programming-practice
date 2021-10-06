/*
	Spread Operator
*/
const numbers = [1,2,3];
const newNumbers = [...numbers, 4]; 

console.log(newNumbers)

const person = {
	name: 'Manu',
	sex: 'Male',
	programmingLanguage: 'JavaScript',
	experience: 4
};

const newPerson = {
	...person,
	age: 28
};

console.log(newPerson)

/*
	Rest Operator
*/

const filt = (...args) =>{
	return args.filter(el => el === 1);
}

console.log(filt(1,2,3));
 