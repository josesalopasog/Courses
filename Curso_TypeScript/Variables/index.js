// Any variables ⬇️:
var anyVariable; // In this variable, we can assign any type of value
anyVariable = 10;
console.log("Value of anyVariable: ".concat(anyVariable));
console.log("Type of anyVariable: ".concat(typeof anyVariable));
// Unknown variables ⬇️:
var unknownVariable; // In this variable, we can assign any type of value too, but we cannot use it  directly without type assertion
unknownVariable = 20;
// unknownVariable = "Hello, World!";
if (typeof unknownVariable === "string") {
    console.log("The unknownVariable is a string. Value: ".concat(unknownVariable));
}
else if (typeof unknownVariable === "number") {
    console.log("The unknownVariable is a number. Value: ".concat(unknownVariable));
}
else {
    console.log("The unknownVariable is of type ".concat(typeof unknownVariable, ". Value: ").concat(unknownVariable));
}
// Void Variables ⬇️:
function logMessage(message) {
    console.log(message);
}
logMessage("This is a void function message.");
// Never variables ⬇️:
function throwError(message) {
    throw new Error(message);
}
throwError("This is an error message.");
