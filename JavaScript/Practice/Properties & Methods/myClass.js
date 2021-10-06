class Human{
    
    gender = 'male';
    
    printGender = () => {
        console.log(this.gender);
    }
} 

class Person extends Human{
    
    name = "Manu";
    gender = 'female'

    printMyname = () =>{
        console.log(this.name);
    }
}

const person  = new Person();
person.printMyname();
person.printGender();


 