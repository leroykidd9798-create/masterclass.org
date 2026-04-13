document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Close mobile menu when clicking a link
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
      }
    });
  });

  // Sticky Header Effect
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
      header.setAttribute('style', 'box-shadow: var(--shadow-md); padding: 12px 0;');
    } else {
      header.setAttribute('style', 'box-shadow: var(--shadow-sm); padding: 16px 0;');
    }
  });

  // Accordion Logic
  const accordionItems = document.querySelectorAll('.accordion-item');
  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    if (header) {
      header.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close all other
        accordionItems.forEach(el => {
          el.classList.remove('active');
          el.querySelector('.accordion-content').style.maxHeight = null;
        });

        // Toggle current
        if (!isActive) {
          item.classList.add('active');
          const content = item.querySelector('.accordion-content');
          content.style.maxHeight = content.scrollHeight + "px";
        }
      });
    }
  });

  // FAB Toggle
  const fabButton = document.querySelector('.fab-button');
  const fabContainer = document.querySelector('.fab-container');
  
  if (fabButton) {
    fabButton.addEventListener('click', (e) => {
      e.stopPropagation();
      fabContainer.classList.toggle('active');
    });
  }

  // Close FAB when clicking outside
  document.addEventListener('click', (e) => {
    if (fabContainer && fabContainer.classList.contains('active') && !fabContainer.contains(e.target)) {
      fabContainer.classList.remove('active');
    }
  });
});
