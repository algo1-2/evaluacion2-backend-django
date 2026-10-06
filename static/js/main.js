// main.js - Scripts complementarios para la aplicación Django
document.addEventListener('DOMContentLoaded', () => {
    // Inicialización de tooltips de Bootstrap si existen
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl));

    console.log('Django Movie Portal - Benjamín Rivas inicializado correctamente.');
});
