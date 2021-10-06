// const manu = {
//     name: 'Manuperro',
//     year: 2020,
//     birth: 1999,

//     getAge: function() {
//         this.age = this.year - this.birth;
//         return this.age;
//     }
// }

// console.log(manu.name);
// console.log(manu.getAge());

class Parent {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

class Child extends Parent {
    constructor(name, age) {
        super(name, age);
    }
}

const pingu = new Parent('Pingu', 21);
const manu = new Child('Manu', 21);



console.log(pingu)
console.log(manu)