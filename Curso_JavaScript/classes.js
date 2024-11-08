//Clases en JavaScript

//Herencia de clases
//Creando una  Clase Padre 
class Persona{
    //Atributos Estaticos: 
    static contadorPersonas = 0; 

    static get MAX_OBJ(){ //Constante de tipo estatico
        return 5;
    }

    //Atributos de nuestros objetos: 
    email = 'Valor default email';

    constructor(nombre,apellido){
        //Atributos
        //Nombre del atributo - Nombre del parametro
        this._nombre = nombre;
        this._apellido = apellido;
        //Las variables estaticas se llaman con el nombre de la clase
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas;
        }else{
            console.log('Se han superado el máximo de objetos permitidos')
        }
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    //Agregando metodos distintos a get y set 
    nombreCompleto(){
        return this.idPersona+'. '+this._nombre+' '+this._apellido;
    }
    //Sobre escribiendo el metodo de la clase Padre (Object)
    toString(){
        //Se aplica polimorfismo(Multiples formas en metodo de ejecución)
        return this.nombreCompleto();
    }
    //Agregando metodos estaticos
    static saludar(){
        console.log('Saludos desde método static')
    }
    static saludar2(persona){
        console.log(`Hola ${persona.nombre}`);
    }
}
//Creando una Clase Hija 
class Empleado extends Persona{
    constructor(nombre,apellido,departamento){
        super(nombre,apellido); //Con super llamamos al constructor de la clase padre para traer sus atributos 
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    //Usando el concepto de sobreescritura para modificar el comportamiento del metodo nombreCompleto()
    nombreCompleto(){
        return super.nombreCompleto()+'-'+this._departamento;
    }
}

//Creando nuevos objetos apartir de nuestra clase
let persona1 = new Persona('Juan','Perez');
console.log(persona1);
//Utilizando el metodo get para traer el nombre 
console.log(persona1.nombre)

let persona2 = new Persona('Carlos','Lara');
console.log(persona2);
//Utilizando el metodo set para cambiar el nombre 
persona2.nombre = 'Luis'
console.log(persona2.nombre);

let empleado1 = new Empleado('David','Garcia','Sistemas');
console.log(empleado1)
console.log(empleado1.nombre);
console.log(empleado1.nombreCompleto());

//Polimorfismo:
console.log(empleado1.toString());

//Utilizando el metodo static
Persona.saludar();
Persona.saludar2(persona1);
Empleado.saludar2(persona2);

//Utilizando atributos static 
console.log(Persona.contadorPersonas);
console.log(Empleado.contadorPersonas);

//LLamando atributos no estaticos
console.log(persona1.email);

console.log(Persona.MAX_OBJ);

let persona3 = new Persona('Carmen','Lara');
let persona4 = new Persona('Mariana','Toledo');
let persona5 = new Persona('Laura','Toledo'); //Limite de objetos permitidos
console.log(persona5.toString())

/*
Reglas/Notas: 
- La clase Object es la clase padre de todas las clases. Esto quiere decir que heredan automaticamente los metodos de la clase Object.
- No se aplica el concepto de Hoisting (Se debe crear primero la clase para crear objetos)
- Para utilizar el concepto de sobreescritura se debe usar el mismo nombre que tiene el metodo de la clase padre.
- El polimorfismo sirve para que diferentes objetos respondan a la misma función o metodo pero de diferentes maneras. 
- Los Metodos Static se asocian directamente con la clase mas no con los objetos que se creen de esta misma. 
*/

