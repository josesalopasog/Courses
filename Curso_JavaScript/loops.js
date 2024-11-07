// Ciclo While 
// Imprimir los valores del 0 al 5
let contador = 0, repeticiones = 5;

while(contador <= repeticiones){
    console.log(contador++);
    //contador++
}
contador = 0
//Ciclo do While (Lo usamos cuando al menos queremos que se ejecute una vez)
do{
    console.log(contador++);
    //contador++
}while(contador <= repeticiones);

//Ciclo For 
for(let i = 0; i<=repeticiones; i++){
    console.log(i)
}

//Ejercicio 1 
//Imprimir los primeros 10 numeros de 3 en 3 
for(let i = 1; i<=10; i += 3){
    console.log(i)
}

//Ejercicio 2 
let acumulador = 0;
for(let i = 1; i<=5; i++){
    acumulador +=  i; 
    console.log(acumulador); 
}

//Ejercicio 3 
let i=1, r=0;
while(i <= 5){
    console.log(r+=i);
    i++;
}
i=1;
r=0;
//Ejercicio 4 
do{
    console.log(r+=i);
    i++;
}while(i <= 5);

