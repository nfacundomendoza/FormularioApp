document.getElementById('copyButton').addEventListener('click', () => {
    const contentElement = document.getElementById('copy-table-wrapper');
    const mensaje = document.getElementById('mensaje');

    const htmlToCopy = contentElement.innerHTML;
    const textToCopy = contentElement.innerText;

    navigator.clipboard.write([
        new ClipboardItem({
            'text/html': new Blob([htmlToCopy], { type: 'text/html' }),
            'text/plain': new Blob([textToCopy], { type: 'text/plain' })
        })
    ]).then(() => {
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
