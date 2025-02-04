document.getElementById('copyButton').addEventListener('click', () => {
    const contentElement = document.getElementById('content');
    const textToCopy = contentElement.innerText;
    const mensaje = document.getElementById('mensaje');

    navigator.clipboard.writeText(textToCopy).then(() => {
        mensaje.classList.remove('d-none', 'fadeout');
        mensaje.classList.add('alert', 'alert-success', 'fadein');

        if (mensaje.dataset.timeoutId) {
            clearTimeout(mensaje.dataset.timeoutId);
        }

        const timeoutId = setTimeout(() => {
            mensaje.classList.add('fadeout');
            setTimeout(() => {
                mensaje.classList.add('d-none');
            }, 1000);
        }, 3000);

        mensaje.dataset.timeoutId = timeoutId;
    }).catch(err => {
        console.error('Error al copiar al portapapeles:', err);
    });
});