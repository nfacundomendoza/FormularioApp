document.getElementById('generatePdfButton').addEventListener('click', () => {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    const content = document.getElementById('content');

  
    const paragraphs = content.querySelectorAll('p');

    doc.setFont("helvetica", "bold");
    doc.setFontSize(18); 
    doc.setFont("helvetica", "normal");
    doc.setFontSize(12);

    let y = 30;
    paragraphs.forEach(paragraph => {
        const text = paragraph.innerText;

        const lines = doc.splitTextToSize(text, 180); 
        doc.text(lines, 10, y); 
        y += lines.length * 10; 

        if (y > 280) { 
            doc.addPage();
            y = 20; 
        }
    });

    const nombreArchivo = document.getElementById('archivo').innerText;
    const nombreSinExtension = nombreArchivo.replace(/\.json$/, '');
    doc.save(nombreSinExtension + '.pdf');
    
});