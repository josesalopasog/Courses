// Methods & Functions in Typescript 
function printMessage(message) {
    console.log(message);
}
printMessage("Hello World!");
var sum = function (x, y) {
    return x + y;
};
var result = sum(5, 10);
console.log("Sum Result: ".concat(result));
// Function with optional parameters ⬇️:
var salute = function (name, doSalute) {
    if (doSalute) {
        return "".concat(doSalute, " ").concat(name);
    }
    else {
        return "The user ".concat(name, " has no salute");
    }
};
console.log(salute("John"));
console.log(salute("John", "Hello"));
function add(x, y) {
    return x + y;
} // Function Overloading allows you to define multiple signatures for a single function.
// This function can take either two numbers or two strings and return the appropriate type.
console.log("Function Overloading: ⬇️");
console.log(add(5, 10));
console.log(add("Hello", "World"));
// Function with default parameters ⬇️:
function greet(name, greeting) {
    if (greeting === void 0) { greeting = "Hello"; }
    return "".concat(greeting, ", ").concat(name, "!");
}
console.log("Default Parameters: ⬇️");
console.log(greet("Jose"));
// Function with rest parameters ⬇️:
function sumAll() {
    var numbers = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        numbers[_i] = arguments[_i];
    }
    return numbers.reduce(function (acc, num) { return acc + num; }, 0); // Reduce the array to a single value
}
console.log("Rest Parameters: ⬇️");
console.log(sumAll(1, 2, 3, 4, 5));
