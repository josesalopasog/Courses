// Any variables ⬇️:
let anyVariable: any; // In this variable, we can assign any type of value

anyVariable = 10;

console.log(`Value of anyVariable: ${anyVariable}`);
console.log(`Type of anyVariable: ${typeof anyVariable}`);

// Unknown variables ⬇️:
let unknownVariable: unknown; // In this variable, we can assign any type of value too, but we cannot use it  directly without type assertion

unknownVariable = 20;
// unknownVariable = "Hello, World!";

if (typeof unknownVariable === "string"){
    console.log(`The unknownVariable is a string. Value: ${unknownVariable}`);

} else if (typeof unknownVariable === "number"){
    console.log(`The unknownVariable is a number. Value: ${unknownVariable}`);
} else{
    console.log(`The unknownVariable is of type ${typeof unknownVariable}. Value: ${unknownVariable}`);
}

// Void Variables ⬇️:
function logMessage(message: string): void { // This function does not return any value, it just logs the message to the console.
    console.log(message);
}

logMessage("This is a void function message.");

// Never variables ⬇️:
function throwError(message: string): never { // This function will never return a value,it will always throw an error or terminate the program
    throw new Error(message);
}

throwError("This is an error message.");

