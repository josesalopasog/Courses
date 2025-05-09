const userDatabase = [ 
    {
        username: "andres",
        password: "123",
    },
    {
        username: "caro",
        password: "456",
    },
    {
        username: "mariana",
        password: "789",
    },
];

const usersTimeLine = [
    {
        username: "Estefany",
        timeline: "Me encanta Javascript",
    },
    {
        username: "Oscar",
        timeline: "Bebeloper es lo mejor!",
    },
    {
        username: "Mariana",
        timeline: "A mi me gusta más el café que el té",
    },
    {
        username: "Andres",
        timeline: "Yo hoy no quiero trabajar",
    },
]

class User {
    constructor(username,pass){
        this._username = username; 
        this._pass = pass; 
    }
    get username(){
        return this._username;
    }
    set username(username){
        this._username = username;
    }

    validation(){
        let msg = ``
        let loginState = false;

        for (let i=0; i<userDatabase.length;i++){
            if((Object.values(userDatabase[i])[0] == this._username) && (Object.values(userDatabase[i])[1] == this._pass)){
                msg = `Usuario Encontrado, Username:${this._username} - Pass:${this._pass}  `;
                loginState = true;
                return {msg,loginState};
            }else{
                msg = "Usuario No encontrado";
                loginState = false;
            }
        }
        return {msg,loginState};
    }
    signIn(flag){
        if(flag == true){
            let user = usersTimeLine.find(user => user.username.toLowerCase() === this._username);
            return user;
        }else{
            return "No pudiste acceder";
        }

    }
    
}

let user1 = new User("andres","123"); 
let user2 = new User("jose","123"); 
let user3 = new User("mariana","789"); 


console.log(user1.validation().msg);
console.log(user2.validation().msg);
console.log(user3.validation().msg);

console.log(user1.validation().loginState);
console.log(user2.validation().loginState);

console.log(user1.signIn(user1.validation().loginState));
console.log(user2.signIn(user2.validation().loginState));
console.log(user3.signIn(user3.validation().loginState));







