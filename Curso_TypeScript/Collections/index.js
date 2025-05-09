var role = ["admin", "user", "guest"];
console.log("Roles: ".concat(role));
var anyArray = [1, "hello", true, null, { name: "John" }];
console.log("Any Array: ".concat(anyArray));
var users = [
    { id: 1, name: "John Doe", email: "johndoe@example.com", age: 30, isAdmin: true },
    { id: 2, name: "Jane Smith", email: "janesmith@example.com", age: 25, isAdmin: false },
];
console.log("Users: ".concat(JSON.stringify(users)));
// Tuples ⬇️:
var userTuple;
userTuple = [1, "John", "Doe", 30, true];
console.log("User Tuple: ".concat(userTuple));
var usersTuple = [];
usersTuple.push([1, "John", "Doe", 30, true]);
usersTuple.push([2, "Jane", "Smith", 25, true]);
usersTuple.push([3, "Jack", "Doe", 22, false]);
usersTuple.forEach(function (user) {
    console.log("User Tuple: ".concat(user[0]));
    var userName = user[1];
    var userLastName = user[2];
    var userAge = user[3];
    var userIsAdmin = user[4];
    console.log("User Name: ".concat(userName, ", User Last Name: ").concat(userLastName, ", User Age: ").concat(userAge, ", User Is Admin: ").concat(userIsAdmin));
});
// Enums ⬇️:
var Days;
(function (Days) {
    Days[Days["Monday"] = 0] = "Monday";
    Days[Days["Tuesday"] = 1] = "Tuesday";
    Days[Days["Wednesday"] = 2] = "Wednesday";
    Days[Days["Thursday"] = 3] = "Thursday";
    Days[Days["Friday"] = 4] = "Friday";
    Days[Days["Saturday"] = 5] = "Saturday";
    Days[Days["Sunday"] = 6] = "Sunday";
})(Days || (Days = {}));
var today = Days.Monday;
console.log("Today is: ".concat(Days[today]));
