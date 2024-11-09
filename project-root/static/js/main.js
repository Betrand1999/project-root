// Add smooth scrolling to all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
  
  // Toggle a mobile navigation menu
  document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.createElement('button');
    navToggle.textContent = 'Menu';
    navToggle.classList.add('nav-toggle');
  
    const nav = document.querySelector('nav ul');
    nav.parentNode.insertBefore(navToggle, nav);
  
    navToggle.addEventListener('click', () => {
      nav.classList.toggle('visible');
    });
  });
  
  // Add hover effects to buttons (example of adding/removing classes)
  const buttons = document.querySelectorAll('button, .btn');
  buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
      button.classList.add('hovered');
    });
    button.addEventListener('mouseleave', () => {
      button.classList.remove('hovered');
    });
  });
  
  // Scroll to top functionality
  const scrollToTopButton = document.createElement('button');
  scrollToTopButton.textContent = 'Top';
  scrollToTopButton.classList.add('scroll-to-top');
  document.body.appendChild(scrollToTopButton);
  
  scrollToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  
  window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
      scrollToTopButton.style.display = 'block';
    } else {
      scrollToTopButton.style.display = 'none';
    }
  });
  