// Interfaces 

interface IUser {
    id: number;
    name: string;
    email: string;
    isAdmin: boolean;
};

let user: IUser = {
    id: 1,
    name: "John Doe",
    email: "jonhdoe@example.com",
    isAdmin: true
}

console.log(`User: ${JSON.stringify(user)}`);

let usersDB : IUser[] = [
    { id: 2, name: "Jane Smith", email: "janesmith@example.com", isAdmin: false},
    { id: 3, name: "Jack Doe", email: "jackdoe@example.com", isAdmin: false},
]

console.log(`Users DB: ${JSON.stringify(usersDB)}`);

// Interfaces and functions ⬇️
interface IAdd {
    (a:number, b:number): number;
}

let add: IAdd = (a:number, b:number): number => {
    return a + b;
}

console.log(`Add: ${add(2,3)}`);

// Interfaces with optional properties ⬇️
interface IProduct{
    id: number;
    name: string;
    price: number;
    description?: string; // optional property
}

let product: IProduct = {
    id: 1,
    name: "Product 1",
    price: 100,
    description: "This is the description of product 1"
}

console.log(`Product: ${JSON.stringify(product)}`); 

// Interfaces with readonly properties ⬇️
interface IAppointments{
    readonly id: number;
    readonly date: Date;
    readonly time: string;
    readonly description: string;
}

let appointment: IAppointments = {
    id: 1,
    date: new Date("2023-10-01"),
    time: "10:00 AM",
    description: "Doctor's appointment"
}

console.log(`Appointment: ${JSON.stringify(appointment)}`);

// appointment.id=2; // Error: Cannot assign to 'id' because it is a read-only property

//Interfaces with extending ⬇️
interface IEmployee extends IUser {
    position: string;
    salary: number;
}

let employee: IEmployee = {
    id: 4,
    name: "Alice Johnson",
    email: "alice.johnson@example.com",
    isAdmin: false,
    position: "Software Engineer",
    salary: 80000
}

console.log(`Employee: ${JSON.stringify(employee)}`);