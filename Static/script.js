fetch("http://127.0.0.1:5000/productos", {
    headers: { "Accept": "application/json" } // Asegura que reciba JSON
})
.then(response => response.json())
.then(data => {
    const productosDiv = document.getElementById("IDproductos"), // DIV de los productos
    preciosDiv = document.getElementById("IDprecios"); // DIV de los precios
    productosDiv.innerHTML = ""; // Limpiar contenido previo
    preciosDiv.innerHTML = ""; // Limpiar contenido previo
    console.log("Json:\n"+data.productos);
    data.productos.forEach(producto => {
        const pProductos = document.createElement("p"),
        pPrecios = document.createElement("p");;
        pProductos.textContent = `${producto.nombre}`;
        pPrecios.textContent = `${producto.precio}`;
        console.log(`${producto.nombre} - $${producto.precio}`);
        productosDiv.appendChild(pProductos);
        preciosDiv.appendChild(pPrecios);
    });
})
.catch(error => console.error("Error al obtener los productos:", error));
