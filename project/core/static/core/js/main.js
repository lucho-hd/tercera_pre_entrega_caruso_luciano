window.addEventListener('scroll', function() {
    let navbar = document.getElementById('navbar');
    let scrollPosition = window.scrollY || document.documentElement.scrollTop;
  
    if (scrollPosition > 100) { 
      navbar.classList.add('navbar-shadow');
    } else {
      navbar.classList.remove('navbar-shadow');
    }
  });
  
  document.addEventListener('DOMContentLoaded', function() {
    const textareas = document.querySelectorAll('textarea');

    textareas.forEach(textarea => {
        const adjustHeight = (textarea) => {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        };

        adjustHeight(textarea);

        textarea.addEventListener('input', () => {
            adjustHeight(textarea);
        });
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
  const editIcon = document.getElementById('icono_edit');
  const fileInput = document.getElementById('imagen_perfil');

  editIcon.addEventListener('click', (e) => {
      e.preventDefault(); 
      fileInput.click(); 
  });
});