// Methods & Functions in Typescript 

function printMessage(message: string): void {
    console.log(message);
}

printMessage("Hello World!");

const sum = (x:number, y:number): number => {
    return x + y;
}

let result = sum(5,10);

console.log(`Sum Result: ${result}`);

// Function with optional parameters ⬇️:
const salute = (name: string, doSalute?: string): string => {
    if (doSalute) {
        return `${doSalute} ${name}`;
    } else{
        return `The user ${name} has no salute`;
    }
}
console.log(salute("John"));
console.log(salute("John", "Hello"));

// Function Overloading ⬇️:
function add(x:number, y:number): number;
function add(x:string, y:string): string;
function add(x:any, y:any): any {
    return x + y;
} // Function Overloading allows you to define multiple signatures for a single function.
// This function can take either two numbers or two strings and return the appropriate type.

console.log("Function Overloading: ⬇️")
console.log(add(5, 6));
console.log(add("Hello", "World"));

// Function with default parameters ⬇️:
function greet(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}!`;
}

console.log("Default Parameters: ⬇️");
console.log(greet("Jose"));

// Function with rest parameters ⬇️:

function sumAll(...numbers: number[]): number {
    return numbers.reduce((acc, num) => acc + num, 0); // Reduce the array to a single value
}

console.log("Rest Parameters: ⬇️");
console.log(sumAll(1,2,3,4,5));