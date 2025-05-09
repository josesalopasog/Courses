let varSize: string = "Hello World!";

console.log(varSize.length);

function getLength<T extends {length: number} >(obj: T): number {
    let len: number = obj.length;
    let type: string = typeof obj;
    console.log(`Type: ${type} - Length: ${len}`);
    return obj.length;
}

console.log(getLength(varSize)); 

console.log(getLength([1,2,3,4,5]));

// extends is used to extend a type or interface, allowing you to create a new type that inherits properties from an existing type or interface.
// This is useful for creating more specific types based on existing ones, enabling code reuse and better type safety.