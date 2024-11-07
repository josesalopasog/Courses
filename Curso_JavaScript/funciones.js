//Procedimiento 
//1. Definir el procedimiento 
function saludar(mensaje){
    //Cuerpo de la funcion
    console.log(`Hola, este fue tu mensaje: ${mensaje}`)
}

//2. Lammar al procedimiento 
saludar(`Feliz tarde`);

//Funciones 
//1. Declarar la funcion 
function sumar(a,b){
    let resultadoSuma = a + b;
    return  resultadoSuma; 
}

//2. Llamar o invocar la funcion 
let resultado = sumar(5,7);
console.log(resultado)

//Paso por valor en JS 
// Aplica cuando estamos pasando información de tipo primitivo (number,bool,string)
function cambiarValor(parametro){
    parametro = 20
}
let argumento = 10; 
cambiarValor(argumento)
console.log(argumento)

//Paso por referencia 
// Objetos (incluyendo arrays) se pasan por referencia 

function cambiarValor2(parametro){
    parametro[0] = 20; 
}
//Llamamos a la funcion 
let arreglo = [10]; 
console.log(arreglo)
cambiarValor2(arreglo);
console.log(arreglo)

//Cadenas inmutables de JS (No se puede modificar su valor)
function cambiarValor3(parametro){
    parametro = 'Adios';
}
//LLamamos a la funcion 
let argumento2 = 'hola';
console.log(argumento2)
cambiarValor3(argumento2)
console.log(argumento2)

//Alcance de Variables en JS 

let variableGlobal = 5; 

//Modificar valor 
variableGlobal = 10; 

//Definición funcion 
function miFuncion(variableLocal){
    console.log(variableLocal);
    variableGlobal = 20;
}
//Llamamos la funcion 
miFuncion(variableGlobal);
console.log(variableGlobal);

//Funcion Recursiva
// 1. Se debe llamar a si misma
// 2. Debe avanzar hacia un caso base, de lo contraria caemos en un ciclo infinito
function funcionRecursiva(numero){
    //Caso Base
    if (numero ==1)
        console.log(numero);
    else{
        console.log(numero);
        funcionRecursiva(numero-1);
    }
}
funcionRecursiva(3);

//Funciones incorporadas en JS 
//Obtener largo de una cadena 
let cadena1 = 'Hola';
console.log(cadena1.length);
//No podemos modificar una cadena JS ya que las cadenas son inmutables
cadena1[0] = 'x';
console.log(cadena1);
//Si podemos asignar una nueva cadena 
cadena1 = 'Adios'
console.log(cadena1)
//Iterando la cadena 
for(let i=0; i<cadena1.length;i++){
    console.log(cadena1[i])
}

//Subcadenas en JS
let cadena2 = 'Hola Mundo';
//substring(indice_inicio, indice_fin+1)
let cadena3 = cadena2.substring(0,4);
let cadena4 = cadena2.substring(5);
console.log(cadena3)
console.log(cadena4)

//Concatenacion de Cadenas en JS 
let cadena5 = cadena3+' '+ cadena4
console.log(cadena5);

//Convertir cadena a numero en JS 
let a = '10', b='20'
console.log(a+b);
//Convertir a numeros para que se sumen 

let suma = parseInt(a)+parseInt(b);
console.log(suma);

let x = 10, y=20
let concatenar = a.toString() + b.toString()
console.log(concatenar)

//Valor absoluto 
let numero = -10;
let valorAbsoluto = Math.abs(numero);
console.log(valorAbsoluto);

//Redondeo y trucado en JS 
let num = 8.5, redondeo, truncado;
//Redondeo 
redondeo = Math.round(num);
console.log(redondeo);
//Truncado 
truncado = Math.trunc(num);
console.log(truncado);