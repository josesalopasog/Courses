//Reglas de nombres de variables:
/* 
- Las variables son sensibles entre mayusculas y minusculas 
- Debe iniciar con una letra o con los simbolos $ o _ 
- Suelen nombrarse con notación de stilo camel case
*/

var miNumero1 = 15;
console.log(miNumero1);

let miNumero2 = 20; 
console.log(miNumero2);

let $miNumero3 = 10; 
console.log($miNumero3);

let _miNumero4 = 30;
console.log(_miNumero4);

let minumero2 = 40;
console.log(minumero2);


//Tipos de datos en JS 
//Datos Numericos: 
let miEntero = 10;
console.log(miEntero);
console.log(typeof miEntero);


let miFlotante = 7.5;
console.log(miFlotante);
console.log(typeof miFlotante);

//Nota: JavaScript engloba los enteros y los flotantes en tipo numericos

//Datos String: 
let miCadena = "Hola";
console.log(miCadena);
console.log(typeof miCadena);

//Datos boleanos: 
let miBoolean = true;
console.log(miBoolean);
console.log(typeof miBoolean);

//Datos nulos: 
let miNull = null;
console.log(miNull);
console.log(typeof miNull);

let miUndefined = undefined;
console.log(miUndefined);
console.log(typeof miUndefined);

//Hoisting (Podemos usar una variable y despues declararla)
var x;  //1. Declarar la variable 
x = 10; //2. Inicializamos la variable

console.log(x); 
//Nota: Esto solo se aplica si la variable se define con 'var'

const MI_CONSTANTE = 10; 

// MI_CONSTANTE = 20 - No podemos cambiar el valor de una constante 

console.log(MI_CONSTANTE);
console.log(Math.PI); //Math es una clase donde traemos la constante PI

//Constante segundos por minuto 
const SEGUNDOS_POR_MINUTO = 60;
console.log(SEGUNDOS_POR_MINUTO);