//Sentencia If
let miNumero = 10;

//Revisar si el numero es positivo 
if(miNumero > 0){
    console.log(`Valor positivo ${miNumero}`);
}else if(miNumero < 0){
    console.log(`Valor Negativo ${miNumero}`);
}else{
    console.log(`Valor cero${miNumero}`)
}

//Operador ternario
(miNumero > 0) ? console.log(`Positivo`) : console.log(`Negativo`)

//Ejercicio 1
//Algoritmo para saber si es mayor de Edad 

const EDAD_ADULTO = 18;
let edadPersona = 7;

//Revisar si la persona es mayor de edad 
if(edadPersona >= EDAD_ADULTO ){
    console.log(`La persona con edad ${edadPersona} es un adulto`)
}else{ 
    console.log(`La persona con edad ${edadPersona} es menor de edad`)
}

//Ejercicio 2 
let diaSemana = 1; 

if(diaSemana == 1){
    console.log('Lunes');
}else if(diaSemana == 2){
    console.log('Martes');
}else if(diaSemana == 3){
    console.log('Miercoles');
}else if(diaSemana == 4){
    console.log('Jueves');
}else if(diaSemana == 5){
    console.log('Viernes');
}else if(diaSemana == 6){
    console.log('Sabado');
}else if(diaSemana == 7){
    console.log('Domingo');
}else{
    console.log('No es un día de la semana');
}

//Sentencia Switch 

switch(diaSemana){
    case 1:
        console.log('Lunes');
        break;
    case 2:
        console.log('Martes');
        break;
    case 3:
        console.log('Miercoles');
        break;
    case 4:
        console.log('Jueves');
        break;
    case 5:
        console.log('Viernes');
        break;
    case 6:
        console.log('Sabado');
        break;
    case 7:
        console.log('Domingo');
        break;
    default:
        console.log('No es un día de la semana');
}
