window.addEventListener('scroll', function() {
    let navbar = document.getElementById('navbar');
    let scrollPosition = window.scrollY || document.documentElement.scrollTop;
  
    if (scrollPosition > 100) { 
      navbar.classList.add('navbar-shadow');
    } else {
      navbar.classList.remove('navbar-shadow');
    }
  });
  