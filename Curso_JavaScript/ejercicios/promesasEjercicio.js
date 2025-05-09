// function fetchData() {
//     fetch("https://rickandmortyapi.com/api/character")
//     .then((response) => response.json())
//     .then((data) => console.log(data))
//     .catch((error) => console.log(error));
// }

async function fetchData(){
    try{
        let response = await fetch("https://rickandmortyapi.com/api/character");
        let data = await response.json();
        console.log(data)
    }catch(error){
        console.log(error)
    }
}

const urls = [
    "https://rickandmortyapi.com/api/character",
    "https://rickandmortyapi.com/api/location",
    "https://rickandmortyapi.com/api/episode",
];

async function fetchNewData() {
    // Define una función asíncrona llamada fetchNewData.
    // Esto permite usar 'await' dentro de la función para manejar promesas.
    try {
        // Intenta ejecutar el bloque de código principal.
        for await (let url of urls) {
            // Recorre de manera asíncrona un iterable llamado 'urls'.
            // Cada iteración espera que la promesa asociada con cada 'url' se resuelva.
            // 'urls' debe ser un iterable que devuelva promesas (por ejemplo, un array de URLs o un generador asíncrono).

            let response = await fetch(url);
            // Realiza una solicitud HTTP GET a la URL actual y espera a que se resuelva la promesa.
            // 'response' contiene el objeto Response devuelto por la función fetch.

            let data = await response.json();
            // Convierte el cuerpo de la respuesta (en formato JSON) a un objeto de JavaScript.
            // Esto también es una operación asíncrona, porque puede tardar en procesar datos grandes.

            console.log(data);
            // Imprime en la consola el contenido del JSON ya convertido en objeto.
        }
    } catch (error) {
        // Si ocurre algún error en cualquier parte del bloque 'try', el flujo salta aquí.
        console.log(error);
        // Imprime el error en la consola para diagnosticarlo.
    }
}