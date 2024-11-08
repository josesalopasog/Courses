//Objetos 
//Un objeto puede tener propiedades y metodos 

//Funcion constructor de objetos de tipo Persona
function Persona(nombre,apellido,email){
    //Propiedad - Parametro
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
//Creando varios objetos de clase persona 
let padre = new Persona('Juan','Perez','jperez@correo.com');
let madre = new Persona('Maria','Garcia','mgarcia@correo.com');

console.log(padre);
console.log(madre);
console.log(padre.nombreCompleto());
console.log(madre.nombreCompleto())

//Otra forma de crear objetos
let miObjeto = new Object();
let miObjeto2 = {};

let miCadena1 = new String('Hola'); //Manera formal
let miCadena2 = 'Hola'; //Manera recomendable

let miNumero = new Number(1); //Manera formal
let miNumero2 = 1; //Manera recomendable

//Usando prototype para agregar atributos a una clase
Persona.prototype.tel = '1234567'

console.log(padre);
console.log(madre);

//Creando un objeto sin constructor
let persona = {
    //Atributos: 
    nombre: 'Juan',
    apellido: 'Perez',
    apellido2: 'Garcia',
    email: 'jperez@gmail.com',
    edad: 28,
    idioma: 'es',
    //Metodos:
    nombreCompleto: function(titulo,tel){
        return titulo+':'+this.nombre +' '+ this.apellido +' '+tel;
    },
    get nombreCompleto2(){ //Con Get JS entiende que esto obtiene información de nuestro objeto
        return this.nombre+' '+this.apellido+' '+this.apellido2;
    },
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    }
}

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.nombreCompleto())
console.log(persona['email'])

persona.tel = '1234567'
delete persona.tel;

//Iterar un objeto 
for (nombrePropiedad in persona){
    console.log(nombrePropiedad)
    console.log(persona[nombrePropiedad])
}

//Otra forma de definir objetos 
let persona2 = new Object();
persona2.nombre = 'Carlos';
persona2.apellido = 'Ramirez';
persona2.direccion = 'Cra123 # 456';
persona2.tel = '123456';

//Usando metodo CALL de JS
console.log(persona.nombreCompleto('Doc','456789'));

console.log(persona.nombreCompleto.call(persona2,'Ing','1234567'));

//Usando el metodo apply
//Se usa similar a Call pero para los nuevos argumentos se usa un arreglo
let arreglo =['Ing','1234567']
console.log(persona.nombreCompleto.apply(persona2, arreglo));

//Formas de imprimir un objeto 

//Concatenando
console.log(persona.nombre +','+persona.apellido)

//Iterar un objeto 
for (nombrePropiedad in persona){
    console.log(nombrePropiedad);
    console.log(persona[nombrePropiedad]);
}
//Con un arreglo 
let personaArray = Object.values(persona);
console.log(personaArray);

let personaString = JSON.stringify(persona);
console.log(personaString);

//Metodos Get y Set 
console.log(persona.nombreCompleto2);
console.log(persona.lang);
persona.lang = 'en';
console.log(persona.idioma);
