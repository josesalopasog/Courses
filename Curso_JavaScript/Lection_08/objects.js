//Objetos 
//Un objeto puede tener propiedades y metodos 

let persona = {
    //Propiedades: 
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'jperez@gmail.com',
    edad: 28,
    //Metodos:
    nombreCompleto: function(){
        return this.nombre +' '+ this.apellido
    }
}

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.nombreCompleto())
console.log(persona['email'])

persona.tel = '1234567'


//Iterar un objeto 
for (nombrePropiedad in persona){
    console.log(nombrePropiedad)
    console.log(persona[nombrePropiedad])
}


//Otra forma de definir objetos 
let persona2 = new Object();
persona2.nombre = 'Carlos';
persona2.apellido = 'Ramirez';
persona2.direccion = 'Cra123 # 456';
persona2.tel = '123456';
