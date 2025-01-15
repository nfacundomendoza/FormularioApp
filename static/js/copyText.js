document.getElementById('copyButton').addEventListener('click', () => {
    const contentElement = document.getElementById('content');
    const textToCopy = contentElement.innerText;

    navigator.clipboard.writeText(textToCopy).then(() => {
        
        mensaje = document.getElementById('mensaje');
        mensaje.className = 'alert alert-success mx-auto w-25 p-2 mt-2';
        
        setTimeout(() => {
            mensaje.className = 'd-none';
        }, 3000);
    }).catch(err => {
        console.error('Error al copiar al portapapeles:', err);
    });
});
