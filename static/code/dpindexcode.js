window.addEventListener('scroll', () => {
    const header = document.getElementById('main-header');
    if (window.scrollY === 0) {
      header.classList.remove('scrolled');
    } else {
      header.classList.add('scrolled');
    }
  });

