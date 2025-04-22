// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips y popovers de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Activar el dropdown al pasar el mouse (hover)
    const dropdownElementList = document.querySelectorAll('.dropdown-hover');
    dropdownElementList.forEach(function(dropdownElement) {
        dropdownElement.addEventListener('mouseenter', function() {
            const dropdown = new bootstrap.Dropdown(this.querySelector('.dropdown-toggle'));
            dropdown.show();
        });
        
        dropdownElement.addEventListener('mouseleave', function() {
            const dropdown = bootstrap.Dropdown.getInstance(this.querySelector('.dropdown-toggle'));
            if (dropdown) {
                dropdown.hide();
            }
        });
    });

    // Animación de aparición en scroll
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    function checkIfInView() {
        const windowHeight = window.innerHeight;
        const windowTopPosition = window.scrollY;
        const windowBottomPosition = windowTopPosition + windowHeight;
        
        animateElements.forEach(function(element) {
            const elementHeight = element.offsetHeight;
            const elementTopPosition = element.getBoundingClientRect().top + windowTopPosition;
            const elementBottomPosition = elementTopPosition + elementHeight;
            
            if ((elementBottomPosition >= windowTopPosition) && (elementTopPosition <= windowBottomPosition)) {
                element.classList.add('animated');
            }
        });
    }
    
    window.addEventListener('scroll', checkIfInView);
    window.addEventListener('resize', checkIfInView);
    window.addEventListener('load', checkIfInView);
    
    // Botón para volver arriba
    const backToTopButton = document.getElementById('back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopButton.classList.add('show');
            } else {
                backToTopButton.classList.remove('show');
            }
        });
        
        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // Función para inicializar botones de detalles de libro
    function initBookDetailButtons() {
        const bookDetailButtons = document.querySelectorAll('.book-detail-btn');
        
        bookDetailButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const bookSlug = this.getAttribute('data-slug');
                loadBookDetails(bookSlug);
            });
        });
    }
    
    // Función para cargar detalles del libro
    function loadBookDetails(slug) {
        fetch(`/libro/${slug}/json/`)
            .then(response => response.json())
            .then(data => {
                // Actualizar contenido del modal con datos del libro
                document.getElementById('modalBookTitle').textContent = data.title;
                document.getElementById('modalBookAuthor').textContent = data.author;
                document.getElementById('modalBookDescription').textContent = data.description;
                document.getElementById('modalBookPrice').textContent = `$${data.price.toFixed(2)}`;
                document.getElementById('modalBookISBN').textContent = data.isbn || 'N/A';
                document.getElementById('modalBookPages').textContent = data.pages || 'N/A';
                document.getElementById('modalBookDate').textContent = data.publication_date || 'N/A';
                
                // Actualizar categorías
                const categoriesElement = document.getElementById('modalBookCategories');
                categoriesElement.innerHTML = '';
                data.categories.forEach(category => {
                    const badge = document.createElement('span');
                    badge.className = 'badge bg-secondary me-1';
                    badge.textContent = category;
                    categoriesElement.appendChild(badge);
                });
                
                // Actualizar portada del libro
                const coverElement = document.getElementById('modalBookCover');
                if (data.cover_url) {
                    coverElement.src = data.cover_url;
                    coverElement.alt = data.title;
                } else {
                    coverElement.src = '/static/images/no-cover.png';
                    coverElement.alt = 'Sin portada';
                }
                
                // Mostrar modal
                const bookModal = new bootstrap.Modal(document.getElementById('bookDetailModal'));
                bookModal.show();
            })
            .catch(error => {
                console.error('Error al cargar detalles del libro:', error);
            });
    }
    
    // Inicializar botones
    initBookDetailButtons();
});
