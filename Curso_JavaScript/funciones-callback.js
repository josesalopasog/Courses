function miFuncion1(){
    console.log('funcion 1');
}

function miFuncion2(){
    console.log('funcion 2');
}

miFuncion1();
miFuncion2();

//Funcion de tipo callback 
function print(mensaje){
    console.log(mensaje);
}
function suma(a,b,funcionCallback){
    let x = a + b;
    funcionCallback(`Resultado: ${x}`);
}

suma(5,3, print);

//Llamadas asíncronas con uso setTimeout
function miFuncionCallback(){
    console.log('saludo asícrontro despues de 3 segundos');
}
setTimeout(miFuncionCallback, 3000);//Despues de 3 segundos (El tiempo esta en ms)

setTimeout(function(){console.log('saludo asíncrono 2')}, 4000);

setTimeout(()=>console.log('Saludo asíncrono 3'),1000);

let reloj=()=>{
    let fecha = new Date();
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`)
}

//setInterval(reloj,1000)

/*---Notas---*/
/*Una función callback es una función que se pasa como argumento 
a otra función para que se ejecute en un momento posterior, 
generalmente cuando la función que la recibe ha terminado su tarea 
o al ocurrir algún evento.*/