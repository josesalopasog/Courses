//Objetos 
//Un objeto puede tener propiedades y metodos 

let persona = {
    //Atributos: 
    nombre: 'Juan',
    apellido: 'Perez',
    apellido2: 'Garcia',
    email: 'jperez@gmail.com',
    edad: 28,
    idioma: 'es',
    //Metodos:
    nombreCompleto: function(){
        return this.nombre +' '+ this.apellido
    },
    get nombreCompleto2(){ //Con Get JS entiende que esto obtiene información de nuestro objeto
        return this.nombre+' '+this.apellido+' '+this.apellido2;
    },
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    }
}

console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.nombreCompleto())
console.log(persona['email'])

persona.tel = '1234567'
delete persona.tel;

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

//Formas de imprimir un objeto 

//Concatenando
console.log(persona.nombre +','+persona.apellido)

//Iterar un objeto 
for (nombrePropiedad in persona){
    console.log(nombrePropiedad);
    console.log(persona[nombrePropiedad]);
}
//Con un arreglo 
let personaArray = Object.values(persona);
console.log(personaArray);

let personaString = JSON.stringify(persona);
console.log(personaString);

//Metodos Get y Set 
console.log(persona.nombreCompleto2);
console.log(persona.lang);
persona.lang = 'en';
console.log(persona.idioma);
