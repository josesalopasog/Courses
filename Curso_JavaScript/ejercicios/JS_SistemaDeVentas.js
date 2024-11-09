class Producto{
    static contadorProdutos = 0; 

    constructor(nombre,precio){
        this._idProducto = ++Producto.contadorProdutos;
        this._nombre = nombre;
        this._precio = precio;
    }
    get idProducto(){
        return this._idProducto;
    }
    get nombre(){
        return this._nombre;
    }
    get precio(){
        return this._precio;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    set precio(precio){
        this._precio = precio;
    }
    toString(){
        return `idProducto:${this._idProducto} Nombre:${this._nombre} Precio:$${this._precio}`
    }
}
class Orden{
    static contadorOrdenes = 0;

    static get MAX_PRODUCTOS(){
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = []; 
        this._contadorProductosAgregados = 0;
    }
    get idOrden(){
        return this._idOrden;
    }
    agregarProducto(producto){
        if(this._productos.length < Orden.MAX_PRODUCTOS){
            this._productos.push(producto); // Se usa el metodo Push para agregar los productos al arreglo 
            //this._producots[this._contadorProductosAgregados++] = prodcuto; 
        }
        else{
            console.log('No se pueden agregar más productos');
        }
    }
    calcularTotal(){
        let totalVenta = 0; 
        for(let producto of this._productos){
            totalVenta += producto.precio; //totalVenta = totalVenta + producto.precio
        }
        return totalVenta
    }
    mostrarOrden(){
        let prodcutosOrden = '';
        for(let producto of this._productos){
            prodcutosOrden += '\n{'+producto.toString()+'}';
        }
        console.log(`Orden: ${this._idOrden} Total: $${this.calcularTotal()}, Productos: ${prodcutosOrden}`)
    }
}


let producto1 = new Producto('Pantalón', 200);
let producto2 = new Producto('Camisa', 100);

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.mostrarOrden();