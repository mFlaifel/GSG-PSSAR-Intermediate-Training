// JavaScript version: same ideas as the Python file, different syntax.

// Print output
console.log("Hi from JavaScript");

// Variable
let age = 25;

// Constant
const MAX_AGE = 120;

// Function
function greet(name) {
    return "Hello, " + name + "!";
}

// If statement
if (age > 18) {
    console.log("Adult");
}

// Array
const skills = ["HTML", "CSS"];

// Object
const student = {
    name: "Sara",
    age: age,
    skills: skills
};

// Use the function and print the data
console.log(greet(student.name));
console.log(student);
console.log("Maximum age:", MAX_AGE);
