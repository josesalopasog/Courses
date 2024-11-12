let miPromesa = new Promise((resolved,rejcted) => {
    let expresion = true;
    if(expresion)
        resolved('Resolvió correcto')
    else
        rejcted('Se produjo un error')
});
//Forma 1 
miPromesa.then(
    valor => console.log(valor),
    error => console.log(error)
);
//Forma 2
miPromesa
.then(valor => console.log(valor))
.catch(error=>console.log(error))

//Ejercicio 1

let promesa = new Promise((resolved)=>{
    console.log('Inicio Promesa')
    setTimeout(()=> resolved('saludos con promesa y timeout'),3000)
    console.log('Fin promesa');
});

promesa.then(valor=>console.log(valor));

//Cuando trabajamos con 'async' indica que una funcion regresa una promesa
async function miFuncionConPromesa() {
    return 'saludos con promesa y async';
}

miFuncionConPromesa().then(valor=> console.log(valor));

//await lo que hace es esperar el resultado de una promesa
async function funcionConPromesaYAwait(){
    let miPromesa = new Promise(resolver =>{
        resolver('Promesa con await')
    });
    
    console.log(await miPromesa);
}

funcionConPromesaYAwait();

//Ejercicio 2 
async function funcionConPromesaAwaitYTimeout(){
    let miPromesa = new Promise(resolver =>{
        setTimeout(()=>resolver('promesa con await y timeout'),3000)
    });
    console.log(await miPromesa);
}

funcionConPromesaAwaitYTimeout();