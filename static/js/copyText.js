document.getElementById('copyButton').addEventListener('click', () => {
    const contentElement = document.getElementById('content');
    const textToCopy = contentElement.innerText;
    const mensaje = document.getElementById('mensaje');

    navigator.clipboard.writeText(textToCopy).then(() => {
        // Mostrar la alerta correctamente
        mensaje.classList.remove('d-none');

        // Si ya hay un timeout en curso, limpiarlo
        if (mensaje.dataset.timeoutId) {
            clearTimeout(mensaje.dataset.timeoutId);
        }

        // Crear un nuevo timeout para ocultar la alerta
        const timeoutId = setTimeout(() => {
            mensaje.classList.add('d-none');
            delete mensaje.dataset.timeoutId; // Eliminar el atributo cuando se oculta
        }, 3000);

        // Guardar el ID del timeout en el dataset
        mensaje.dataset.timeoutId = timeoutId;
    }).catch(err => {
        console.error('Error al copiar al portapapeles:', err);
    });
});
