function sendHeartbeat() {
    fetch('/heartbeat', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({}) 
    })
    .then(response => {
        if (!response.ok) {
            console.error('Error al enviar heartbeat');
        }
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
    });
}

window.onload = function() {
    sendHeartbeat(); 
    setInterval(sendHeartbeat, 600000);
};