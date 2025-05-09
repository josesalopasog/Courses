// Interfaces 
;
var user = {
    id: 1,
    name: "John Doe",
    email: "jonhdoe@example.com",
    isAdmin: true
};
console.log("User: ".concat(JSON.stringify(user)));
var usersDB = [
    { id: 2, name: "Jane Smith", email: "janesmith@example.com", isAdmin: false },
    { id: 3, name: "Jack Doe", email: "jackdoe@example.com", isAdmin: false },
];
console.log("Users DB: ".concat(JSON.stringify(usersDB)));
var add = function (a, b) {
    return a + b;
};
console.log("Add: ".concat(add(2, 3)));
var product = {
    id: 1,
    name: "Product 1",
    price: 100,
    description: "This is the description of product 1"
};
console.log("Product: ".concat(JSON.stringify(product)));
var appointment = {
    id: 1,
    date: new Date("2023-10-01"),
    time: "10:00 AM",
    description: "Doctor's appointment"
};
console.log("Appointment: ".concat(JSON.stringify(appointment)));
var employee = {
    id: 4,
    name: "Alice Johnson",
    email: "alice.johnson@example.com",
    isAdmin: false,
    position: "Software Engineer",
    salary: 80000
};
console.log("Employee: ".concat(JSON.stringify(employee)));
