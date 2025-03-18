 fetch('http://127.0.0.1:5000/productos')
 .then(response => response.json())  // Parsear la respuesta JSON
 .then(productos => {
    const $productosDiv = document.getElementById('productos');
     productos.forEach(producto => {
         // Crear un elemento para cada producto y agregarlo a la página
         const $componenteP = document.createElement("p"),
         $label = document.createElement("label");
         $label.textContent = `${producto.nombre} - $${producto.precio}`;
         $productosDiv.appendChild($label);
     });
 })
 .catch(error => console.error('Error al obtener los productos:', error));