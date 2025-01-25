document.addEventListener('DOMContentLoaded', function () {
    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(function (alert) {
            alert.classList.add('fadeout');
            setTimeout(() => {
                alert.style.display = 'none';
            }, 1000);
        });
    }, 3000);
});
