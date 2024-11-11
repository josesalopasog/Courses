"use strict"

try{
    let x=10;
    //miFunction();
    throw 'Mi error';
}
catch(error){
    console.log(error);
}
finally{
    console.log('Termina la revisión de errores');
}

console.log('continuamos...');

//-------Ejercicio----------
let resultado = 'hola;'
try{
    x=10; 
    if(isNaN(resultado)) throw 'No es un numero';
    else if(resultado === '') throw 'Es una cadena vacía'
}
catch(error){
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally{
    console.log('Termina revisión de errores');
}
