export class User {
    protected id: number; //Protected properties can be only accessed within the class and its subclasses.
    public name: string; //Public properties can be accessed from anywhere.
    private isAdmin: boolean; //Private properties can be accessed only within the class.
    
    constructor(id: number, name: string, isAdmin: boolean) {
        this.id = id;
        this.name = name;
        this.isAdmin = isAdmin;
    }

    public salute(): string {
        return `Hello, my name is ${this.name}`;
    }

    protected getId(): number{
        return this.id;
    }
    private getIsAdmin(): boolean{
        return this.isAdmin;
    }
}

