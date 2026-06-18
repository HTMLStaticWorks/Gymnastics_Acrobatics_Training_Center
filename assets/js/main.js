// main.js
document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Load saved theme or check OS preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        htmlElement.setAttribute('data-theme', 'dark');
        updateThemeIcon('dark');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = htmlElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeToggleBtn) return;
        if (theme === 'dark') {
            themeToggleBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></svg>';
        } else {
            themeToggleBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
        }
    }

    // RTL Toggle
    const rtlToggleBtn = document.getElementById('rtl-toggle');
    
    // Load saved direction
    const savedDir = localStorage.getItem('direction');
    if (savedDir) {
        htmlElement.setAttribute('dir', savedDir);
        updateRtlIcon(savedDir);
    }

    if (rtlToggleBtn) {
        rtlToggleBtn.addEventListener('click', () => {
            const currentDir = htmlElement.getAttribute('dir') || 'ltr';
            const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
            
            htmlElement.setAttribute('dir', newDir);
            localStorage.setItem('direction', newDir);
            updateRtlIcon(newDir);
        });
    }

    function updateRtlIcon(dir) {
        if (!rtlToggleBtn) return;
        if (dir === 'rtl') {
            rtlToggleBtn.textContent = 'LTR';
        } else {
            rtlToggleBtn.textContent = 'RTL';
        }
    }

    // Password Toggle
    const passwordToggles = document.querySelectorAll('.password-toggle');
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const input = this.previousElementSibling;
            if (input.type === 'password') {
                input.type = 'text';
                this.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>';
            } else {
                input.type = 'password';
                this.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>';
            }
        });
    });
    // Active Nav Link
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinksList = document.querySelectorAll('.nav-links .nav-link');
    navLinksList.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Back to top
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Hero Card Stack Interactivity
    const stackCards = document.querySelectorAll('.stack-card');
    if (stackCards.length > 0) {
        stackCards.forEach(card => {
            card.addEventListener('click', function() {
                const container = this.parentElement;
                const allCards = Array.from(container.querySelectorAll('.stack-card'));
                
                // Remove existing order classes
                allCards.forEach(c => {
                    c.classList.remove('c1', 'c2', 'c3');
                });
                
                // Assign c1 (front) to the clicked card
                this.classList.add('c1');
                
                // Assign c2 and c3 to the remaining cards
                let otherIndex = 2;
                allCards.forEach(c => {
                    if (c !== this) {
                        c.classList.add('c' + otherIndex);
                        otherIndex++;
                    }
                });
            });
        });
    }

    // Mobile Menu & Dynamic Action Button Moving
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    const navActions = document.querySelector('.nav-actions');

    if (mobileMenuBtn && navLinks && navActions) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });

        // Automatically move nav-actions into nav-links for mobile view
        const checkMobileMenu = () => {
            if (window.innerWidth <= 1024) {
                // Move action buttons inside nav-links if not already there
                let mobileActionsContainer = navLinks.querySelector('.mobile-actions-wrapper');
                if (!mobileActionsContainer) {
                    mobileActionsContainer = document.createElement('div');
                    mobileActionsContainer.className = 'mobile-actions-wrapper';
                    
                    // Move all children except mobile-menu-btn
                    Array.from(navActions.children).forEach(child => {
                        if (!child.classList.contains('mobile-menu-btn')) {
                            mobileActionsContainer.appendChild(child);
                        }
                    });
                    navLinks.appendChild(mobileActionsContainer);
                }
            } else {
                // Restore to nav-actions
                const wrapper = navLinks.querySelector('.mobile-actions-wrapper');
                if (wrapper) {
                    Array.from(wrapper.children).forEach(child => {
                        navActions.insertBefore(child, mobileMenuBtn);
                    });
                    wrapper.remove();
                }
                navLinks.classList.remove('active'); // Close menu on resize to desktop
            }
        };

        window.addEventListener('resize', checkMobileMenu);
        checkMobileMenu(); // Initial check
    }
});
