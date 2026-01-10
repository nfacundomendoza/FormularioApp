document.getElementById('generatePdfButton').addEventListener('click', () => {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const table = document.querySelector('#copy-table-wrapper table');

    doc.setFont("helvetica", "normal");
    doc.setFontSize(12);

    let y = 20;
    const pageHeight = 280;
    const marginLeft = 10;
    const maxWidth = 180;

    table.querySelectorAll('tr').forEach(row => {
        let line = '';

        const singleCell = row.querySelector('td[colspan="4"]');
        if (singleCell) {
            line = singleCell.innerText.trim();
        } else {
            const cells = row.querySelectorAll('th, td');
            let parts = [];
            for (let i = 0; i < cells.length; i += 2) {
                const label = cells[i]?.innerText.trim() || '';
                const value = cells[i + 1]?.innerText.trim() || '';
                parts.push(`${label}: ${value}`);
            }
            line = parts.join('    ');
        }

        const lines = doc.splitTextToSize(line, maxWidth);

        lines.forEach(l => {
            if (y > pageHeight) {
                doc.addPage();
                y = 20;
            }
            doc.text(l, marginLeft, y);
            y += 8;
        });

        y += 4;
    });

    const nombreArchivo = document.getElementById('nombre-paciente').innerText;
    const nombreSinExtension = nombreArchivo.replace("Nombre del Paciente: ", '');
    doc.save(nombreSinExtension + '.pdf');
});