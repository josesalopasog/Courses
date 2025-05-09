let role: string[] = ["admin","user","guest"];
console.log(`Roles: ${role}`);

let anyArray: any[] = [1,"hello", true, null, {name:"John"}];
console.log(`Any Array: ${anyArray}`);

// Interfaces ⬇️:
interface User {
    id: number;
    name: string;
    email: string;
    age: number;
    isAdmin: boolean;
}

let users: User[] = [
    { id: 1, name: "John Doe", email: "johndoe@example.com", age: 30, isAdmin: true},
    { id: 2, name: "Jane Smith", email: "janesmith@example.com", age: 25, isAdmin: false},
]

console.log(`Users: ${JSON.stringify(users)}`);


// Tuples ⬇️:
let userTuple: [number,string,string,number,boolean];
userTuple = [1,"John", "Doe", 30, true];

console.log(`User Tuple: ${userTuple}`);

let usersTuple: [number,string,string,number,boolean][] = [];

usersTuple.push([1,"John", "Doe", 30, true]);
usersTuple.push([2,"Jane", "Smith", 25, true]);
usersTuple.push([3,"Jack", "Doe", 22, false]);

usersTuple.forEach((user) => {
    console.log(`User Tuple: ${user[0]}`);

    let userName: string = user[1];
    let userLastName: string = user[2];
    let userAge: number = user[3];
    let userIsAdmin: boolean = user[4];

    console.log(`User Name: ${userName}, User Last Name: ${userLastName}, User Age: ${userAge}, User Is Admin: ${userIsAdmin}`);
});

// Enums ⬇️:
enum Days{
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
}

let today: Days = Days.Monday;
console.log(`Today is: ${Days[today]}`);
