fetch("http://127.0.0.1:5000/productos", {
    headers: { "Accept": "application/json" } // Asegura que reciba JSON
})
.then(response => response.json())
.then(data => {
    const productosDiv = document.getElementById("productos");
    productosDiv.innerHTML = ""; // Limpiar contenido previo

    data.productos.forEach(producto => {
        const p = document.createElement("p");
        p.textContent = `${producto.nombre} - $${producto.precio}`;
        console.log(`${producto.nombre} - $${producto.precio}`);
        productosDiv.appendChild(p);
    });
})
.catch(error => console.error("Error al obtener los productos:", error));
