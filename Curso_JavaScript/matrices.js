//Matrices en JS 
//Declaración de una matriz 

let matriz = [[],[]]

//Modificar los valores 
//Reglon 0
matriz[0][0] = 100;
matriz[0][1] = 200;
matriz[0][2] = 300;
//Reglon 1
matriz[1][0] = 400;
matriz[1][1] = 500;
matriz[1][2] = 600;

//Leeer valores 
console.log(matriz[0][1]);

//Sintaxis simplificada

let matriz2 = [[100,200,300],[400,500,600]]
console.log(matriz[0][2]);
console.log(matriz2.length);
console.log(matriz2[0].length);
console.log(matriz2[1].length);


//Iterar una matriz 
for(let i=0; i<matriz2.length; i++){
    for(let j=0; j<matriz2[i].length ; j++){
        console.log(matriz[i][j])
    }
}
