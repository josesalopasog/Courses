// Arrays 
let numerosArreglo = [];
//Modificar los valores 
numerosArreglo[0] = 13; 
numerosArreglo[1] = 21; 
numerosArreglo[4] = 'hola'; 
//Leer los valores 
console.log(numerosArreglo[0]);

//Sintaxis simplificada

let numerosArreglo2 = [13,21,'hola'];
console.log(numerosArreglo2[2]);

//Iterar en los arreglos 
for(let i =0; i< numerosArreglo.length; i++){
    console.log(numerosArreglo[i])
}

const numbersLength = numerosArreglo.length;
console.log(numbersLength);

//Mutability

numerosArreglo.push("bye");
console.log(numerosArreglo);

//Inmutability
const newArray = numerosArreglo.concat("new array");
console.log(newArray);

//Comprobar arrays con el metodo .isArray 
const isArray = Array.isArray(numerosArreglo);
console.log(isArray);

//Suma de los elementos en un array 
let sum = 0; 
const numbersX = [1,2,3,4,5]

for (let i=0; i< numbersX.length; i++){
    sum += numbersX[i];
}
console.log(sum);

// Metodo Push()
const countries =  ['Usa','Colombia','Mexico'];
const countriesLength = countries.push('España','Argentina');
const typeCL =  typeof countriesLength; 

console.log(countries);
console.log(countriesLength);
console.log(typeCL);

// Metodo Pop() - Elimina el ultimo valor del arreglo

const rmvCountry = countries.pop();

console.log(countries);
console.log(rmvCountry);

// Metodo Map() - Itera sobre los elementos y ejecuta un función en especifico

const numbersXSquare = numbersX.map(i => i*i);

console.log(numbersXSquare);

// Metodo forEach() 

const colors = ['red','green','blue']; 
const iteratedColors = colors.forEach(color => console.log(color)) ;

console.log(iteratedColors);

//Ejercicio: F° to C°
const farenheitTemps = [32,68,95];
const celsiusTemps = farenheitTemps.map(t => (5/9)*(t-32));

console.log(farenheitTemps);
console.log(celsiusTemps);

//Ejercicio suma de elementos 

let sum2 = 0; 

numbersX.forEach(n => {
    sum2 += n;
})

console.log(sum2);

//Metodo filter()

const evenNums = numbersX.filter(i => i%2 ===0);

console.log(evenNums);

//Metodo reduce()
//Caso 1 

const sum3 = numbersX.reduce((accumulator, currentValue) => accumulator + currentValue,0);

console.log(sum3);

//Caso 2 
const dic = ['apple','book','cat','dog','cat','dog'];

const wordFreq = dic.reduce((accumulator,currentValue) => {
    if(accumulator[currentValue]){
        accumulator[currentValue]++;
    }else{
        accumulator[currentValue] = 1;
    }
    return accumulator;
}, {});

console.log(wordFreq);

//Metodo find();

const numbersFiveMul = [5,10,15,20,25];
const firstNumGreaterThan10 = numbersFiveMul.find(number => number >10);

console.log(firstNumGreaterThan10);

//Metodo findIndex(); 

const indexGreaterThan10 = numbersFiveMul.findIndex(number => number >10);

console.log(indexGreaterThan10);

//Metodo slice();
 const animals = dic.slice(2,4);

console.log(animals);

//Spread Operator 
const numbersY = [...numbersX];
console.log(numbersY);

const numbersXY = [...numbersX,...numbersY];
console.log(numbersXY);

const numbersZ = [...numbersY,6,7,8];
console.log(numbersZ);