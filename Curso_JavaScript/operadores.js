//Los operadores nos permiten realizar operaciones al usar valores y variables

//Operadores aritmetivos 
/*
+ = Suma
- = Resta 
* = Multiplicación 
/ = División 
% = Modulo 
** = Potencia 
++ = Incremento 
-- = Decremento
*/


let a,b,c,d,e,f;

//Ejemplos: 

a = 3 + 4; 
console.log(a);

b = 6 - 2;
console.log(b);

c = a * 2;
console.log(c);

d = b /2.5;
console.log(d);
console.log(typeof d);

f = 9 % 2; 
console.log(f);

e = 2 ** 3; 
console.log(e);

//Pre-incremento
++a;
console.log(a);

//Post-incremento
a++;
console.log(a);

//Pre-decremento 
--a;
console.log(a);

//Post-decrenebto
a-- 
console.log(a)

//Operadores de asignación 
let miNumero = 20; 

// Operadores compuestos 
miNumero +=5;
console.log(miNumero);

miNumero -=3;
console.log(miNumero);

miNumero *=2;
console.log(miNumero);

miNumero /= 4;
console.log(miNumero);

miNumero %=3; 
console.log(miNumero);

miNumero **=2;
console.log(miNumero);

// Operadores Relacioneales (de comparación)
let num1 = 5;
let num2 = '5';

//Operadores igualdad(Solo compara valores y hace una converción si es necesario);
console.log("num1 == num2 ->", num1==num2)

//Operador de igualdad estricta o exacto (Se compara el valor y el tipo de dato)
console.log("num1 === num2 ->", num1===num2)
//String interpolation
console.log(`${num1} === ${num2} -> ${num1===num2}`);

//Operador distintos (compara valor y convierte el tipo de dato si es necesario)
console.log(`${num1} != ${num2} -> ${num1 != num2}`) 

//Operador disntinto exacto (comopara el valor y el tipo de dato)
console.log(`${num1} !== ${num2} -> ${num1 !== num2}`)

//Operador menor que
console.log(`${num1} < ${num2} -> ${num1 < num2}`)

//Operador menor o igual que 
console.log(`${num1} <= ${num2} -> ${num1 <= num2}`)

//Operador mayor que
console.log(`${num1} > ${num2} -> ${num1 > num2}`)

//Operador menor o igual que 
console.log(`${num1} >= ${num2} -> ${num1 >= num2}`)

//Operadores logicos 
/*
&& = and 
|| = or 
! = not 
*/

let T = true;
let F = false;

//Operador Logico && (and o Y)
console.log(`${T} && ${T} -> ${T && T}`);
console.log(`${T} && ${F} -> ${T && F}`);
console.log(`${F} && ${T} -> ${F && T}`);
console.log(`${F} && ${F} -> ${F && F}`);

//Operador Logico || (OR o O)
console.log(`${T} || ${T} -> ${T || T}`);
console.log(`${T} || ${F} -> ${T || F}`);
console.log(`${F} || ${T} -> ${F || T}`);
console.log(`${F} || ${F} -> ${F || F}`);

//Operador Not 
console.log(`!${T} -> ${!T}`);
console.log(`!${F} -> ${!F}`);

//Ejercicio (Valor dentro de rango)
let min = 0, max = 5;
let dato = 3; 
let dentroRango = dato >= min && dato <= max;

console.log('Valor dentro de rango', dentroRango)