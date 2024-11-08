//Clase Padre 
class Persona{ //Creamos la clase persona 

    static contadorPersonas = 0; //Creamos el atributo estatico para contar los obejtos de clase persona que se crean
    static contadorEmpleados = 0; 
    static contadorClientes = 0;

    constructor(nombre,apellido,edad){
        this._idPersona = ++Persona.contadorPersonas; //Se va asignar el id según los objetos que se vayan creando.
        this._nombre = nombre; 
        this._apellido = apellido;
        this._edad = edad;
    }
    //Metodos Get
    get idPersona(){
        return this._idPersona
    }
    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }
    get edad(){
        return this._edad;
    }
    //Metodos Set 
    set nombre(nombre){
        this._nombre = nombre;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    set edad(edad){
        this._edad = edad;
    }
    //Otros Metodos 
    toString(){
        return `${this._idPersona}-${this._nombre}-${this._apellido}-${this._edad}`
    }       
}
//Clases hijas 
class Empleado extends Persona{
    constructor(nombre,apellido,edad,sueldo){
        super(nombre,apellido,edad); //Llamamos los atributos de la clase padre 
        this._sueldo = sueldo;
        this._idEmpleado = ++Persona.contadorEmpleados;
    }
    //Metodos Get 
    get idEmpleado(){
        return this._idEmpleado;
    }
    get sueldo(){
        return this._sueldo;
    }
    //Metodos Set 
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    //Otros Metodos
    toString(){
        return super.toString()+`-${this._sueldo}-${this._idEmpleado}`;
    }
}
class Cliente extends Persona{
    constructor(nombre,apellido,edad,fechaRegistro){
        super(nombre,apellido,edad);
        this._fechaRegistro = new Date(fechaRegistro);
        this._idCliente = ++Persona.contadorClientes;
    }
    //Metodos Get 
    get idCliente(){
        return this._idCliente;
    }
    get fechaRegistro(){
        return this._fechaRegistro;
    }
    //Metodos Set 
    set fechaRegistro(fechaRegistro){
        this._fechaRegistro =fechaRegistro;
    }
    //Otros Metodos
    toString(){
        return super.toString()+`-${this._fechaRegistro}-${this.idCliente}`;
    }
}

//Creando los objetos
let empleado1 = new Empleado('Juan','Perez',25,4000000)
let empleado2 = new Empleado('Luis','Ramirez',26,4100000)
console.log(empleado1.toString())
console.log(empleado2)

let cliente1 = new Cliente('David','Acosta',27,"2024-11-07")
let cliente2 = new Cliente('Cristian','Garcia',28,"2024-11-08")
console.log(cliente1.toString())
console.log(cliente2)
