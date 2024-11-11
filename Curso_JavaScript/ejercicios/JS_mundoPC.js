//-------Clases Padre------// 
class DispositivoEntrada{
    constructor(tipoEntrada,marca){
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }
    get tipoEntrada(){
        return this._tipoEntrada;
    }
    get marca(){
        return this._marca;
    }
    set tipoEntrada(tipoEntrada){
        this._tipoEntrada = tipoEntrada;
    }
    set marca(marca){
        this._marca = marca; 
    }
    toString(){
        return `Tipo de Entrada: ${this._tipoEntrada} - Marca: ${this._marca}`
    }
}
//-------Clases Hija------// 
class Raton extends DispositivoEntrada{

    static contadorRatones = 0; 

    constructor(tipoEntrada,marca){
        super(tipoEntrada,marca);
        this._idRaton = ++Raton.contadorRatones;
    }
    get idRaton(){
        return this._idRaton;
    }
    toString(){
        return `ID: ${this._idRaton} - ${super.toString()}`
    }
}
class Teclado extends DispositivoEntrada{

    static contadorTeclados = 0; 

        constructor(tipoEntrada,marca){
        super(tipoEntrada,marca);
        this._idTeclado = ++Teclado.contadorTeclados;
    }
    get idTeclado(){
        return this._idTeclado;
    }
    toString(){
        return `ID: ${this._idTeclado} - ${super.toString()}`
    }
}
//-------Cales Independientes------//
class Monitor{

    static contadorMonitores = 0;

    constructor(marca,tamaño){
        this._marca = marca;
        this._tamaño = tamaño; 
        this._idMonitor = ++Monitor.contadorMonitores;
    }
    get marca(){
        return this._marca;
    }
    get tamaño(){
        return this._tamaño; 
    }
    get idMonitor(){
        return this._idMonitor; 
    }
    set marca(marca){
        this._marca = marca;
    }
    set tamaño(tamaño){
        this._tamaño = tamaño;
    }
    toString(){
        return `ID: ${this._idMonitor} - Marca: ${this._marca} - Tamaño: ${this._tamaño}`
    }
}
class Computadora{
    
    static contadorComputadoras = 0;
    
    constructor(nombre,monitor,teclado,raton){
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._teclado = teclado;
        this._raton = raton;
    }
    get idComputadora(){
        return this._idComputadora;
    }
    get nombre(){
        return this._nombre;
    }
    get monitor(){
        return this._monitor;
    }
    get teclado(){
        return this._teclado;
    }
    get raton(){
        return this._raton;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    set monitor(monitor){
        this._monitor = monitor;
    }
    set teclado(teclado){
        this._teclado = teclado;
    }
    set raton(raton){
        this._raton = raton;
    }
    toString(){
        return `ID Computadora: ${this._idComputadora}
                    Nombre: ${this._nombre}
                    Monitor: ${this._monitor}
                    Raton: ${this._raton}
                    Teclado: ${this._teclado}`
    }
}
class Orden{

    static contadorOrdenes = 0;

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = [];
    }
    get idOrden(){
        return this._idOrden;
    }
    agregarComputadora(computadora){
        this._computadoras.push(computadora);
    }
    mostrarOrden(){
        let computadorasOrden = '';
        for(let i of this._computadoras){
            computadorasOrden = '\n{'+i.toString()+'}'
        }
        console.log(`ID Orden:${this._idOrden} - Computadora:${computadorasOrden}`)
    }
}

//-------Creación de ratones-------//
let raton1 = new Raton("USB","Dell");
let raton2 = new Raton("USB","Logitech");
console.log(raton1.toString());

//-------Creación de teclados-------//
let teclado1 = new Teclado("USB","Dell");
let teclado2 = new Teclado("WL","Logitech");
console.log(teclado1.toString());

//-------Creación de monitores-------//
let monitor1 = new Monitor("Dell","45 in.");
let monitor2 = new Monitor("Samsung","50 in.");
console.log(monitor1.toString());

//-------Creación de computadoras-------//
let computador1 = new Computadora("miPc-1",monitor1,raton1,teclado1);
let computador2 = new Computadora("miPc-2",monitor2,raton2,teclado2);
console.log(computador1.toString());
console.log(computador2.toString());

//-------Creación de ordeness-------//
let orden1 = new Orden();
orden1.agregarComputadora(computador1);
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(computador2);
orden2.mostrarOrden();