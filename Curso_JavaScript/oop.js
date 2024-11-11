//------Polimorfismo------//
class Empleado{
    constructor(nombre,sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo; 
    }
    obtenerDetalles(){
        return `Empleado: nombre: ${this._nombre}, Sueldo: ${this._sueldo}`
    }
}

class Gerente extends Empleado{
    constructor(nombre,sueldo,departamento){
        super(nombre,sueldo)
        this._departamento = departamento;
    }
    obtenerDetalles(){
        return `Gerente: Dpto: ${this._departamento} ${super.obtenerDetalles()}`
    }
}

function print(tipo){
    console.log(tipo.obtenerDetalles());
    if(tipo instanceof Gerente){
        console.log('Es un objeto de tipo Gerente');
    }
    else if(tipo instanceof Empleado){
        console.log('Es un oobjeto de tipo Empleado')
    }
}

let empleado1 = new Empleado('Juan',3000);
let gerente1 = new Gerente('Carlos',5000,'Sistemas');

print(empleado1);
print(gerente1);
