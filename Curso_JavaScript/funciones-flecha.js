let miFuncion = function (){
    console.log('Saludos desde mi función')
}

const miFuncionFlecha = () => {
    console.log('Saludos desde mi funcion flecha')
}

const miFuncionFlecha2 = () => console.log('Saludos desde la segunda funcion flecha')

const miFuncionFlecha3 = () => {
    return 'Saludos desde mi función flecha 3'
}

const miFuncionFlecha4 = () => 'Saludos desde mi función flecha 4'

const regresaObjeto = () => ({nombre: 'Juan', apellido: 'Lara'});
console.log(regresaObjeto());

const funcionConParametros = (mensaje) => console.log(mensaje);

const suma = (a,b) => console.log(a+b);

miFuncion();

miFuncionFlecha();

funcionConParametros('Hola');

suma(5,3);

//-----Notas-----//
/*
1. En las funciones flechas no funciona el concepto de hoisting.
2. Como ventaja son funciones mas concisas en comparación a la forma tradicional. Ideal para proyectos mas grandes.
*/