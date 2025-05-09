function identity<T>(arg: T): T {
    return arg;
}

let output1 = identity<string>("Hello World");
let output2 = identity<number>(42);

console.log(output1);
console.log(output2);

// Generic functions are used to create reusable functions that can work with any data type.
// They are defined using angle brackets <> and can take one or more type of parameters.
// identity represents a generic function that takes a single argument of type T and returns a value of the same type T.
// The type parameter T is a placeholder for the actual type that will be pased when the function is called. 