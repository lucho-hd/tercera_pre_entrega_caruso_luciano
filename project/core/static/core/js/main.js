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
        // Function to adjust the height
        const adjustHeight = (textarea) => {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        };

        adjustHeight(textarea);

        // Adjust the height on input
        textarea.addEventListener('input', () => {
            adjustHeight(textarea);
        });
    });
});