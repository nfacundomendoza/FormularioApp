document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.alert').forEach(function (alert) {
        if (alert.id !== 'mensaje') {
            alert.classList.add('fadein'); 
            setTimeout(() => {
                alert.classList.remove('fadein');
            }, 9000); 
        }
    });

    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(function (alert) {
            if (alert.id !== 'mensaje') {
                alert.classList.add('fadeout'); 
                setTimeout(() => {
                    alert.style.display = 'none'; 
                }, 1000);
            }
        });
    }, 16000);
});