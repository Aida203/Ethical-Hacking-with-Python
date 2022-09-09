var carName = "Volvo";
var carName;

console.log(carName)

//Constant Objects and Arrays
/*Change the elements of constant array
Change the properties of constant object */

// You can create a constant array:
const cars = ["Saab", "Volvo", "BMW"];


//Functions
function myFunction(p1, p2) {
    return p1 * p2;   // The function returns the product of p1 and p2
  }

  let x = myFunction(4, 3); 
  console.log(x)

  //objects
  const car = {type:"Fiat", model:"500", color:"white"};

  /*or 
  const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
 */

//accessing
//console.log(car.color)

//object with function

const person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue",
  
    //function
    fullName : function() {
      return this.firstName + " " + this.lastName;}

    }

    console.log(person.fullName() )

    
