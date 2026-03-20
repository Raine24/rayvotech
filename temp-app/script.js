document.addEventListener('DOMContentLoaded', () => {

    // --- Initial Loader Logic ---
    const loader = document.getElementById('initial-loader');
    if(loader) {
        // Simulate loading time to show off the spinner and progress bar
        setTimeout(() => {
            loader.classList.add('hidden');
            setTimeout(() => loader.remove(), 500); // Remove from DOM after fade
        }, 1500);
    }
    
    // --- Custom Cursor Logic ---
    const cursorDot = document.querySelector('[data-cursor-dot]');
    const cursorOutline = document.querySelector('[data-cursor-outline]');
    
    // Check if device supports hover (not a touch device)
    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

    if (!isTouchDevice && cursorDot && cursorOutline) {
        window.addEventListener('mousemove', (e) => {
            const posX = e.clientX;
            const posY = e.clientY;

            // Immediate position for dot
            cursorDot.style.left = `${posX}px`;
            cursorDot.style.top = `${posY}px`;

            // Smooth delayed position for outline
            cursorOutline.animate({
                left: `${posX}px`,
                top: `${posY}px`
            }, { duration: 500, fill: "forwards" });
        });

        // Hover Effects for links and buttons
        const interactables = document.querySelectorAll('a, button, .bento-item, .project-card');
        
        interactables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursorOutline.classList.add('cursor-hover');
                cursorDot.style.backgroundColor = 'transparent';
            });
            
            el.addEventListener('mouseleave', () => {
                cursorOutline.classList.remove('cursor-hover');
                cursorDot.style.backgroundColor = 'var(--color-accent)';
            });
        });
    }

    // --- Global Scroll Handles: Navbar, Parallax, Progress Bar ---
    const navbar = document.querySelector('.navbar');
    const progressBar = document.getElementById('reading-progress');
    const parallaxLayers = document.querySelectorAll('.parallax-layer');
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;

        // Navbar Logic
        if (scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Reading Progress Indicator (Top Bar)
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollY / docHeight) * 100;
        if (progressBar) {
            progressBar.style.width = `${scrollPercent}%`;
        }

        // Extremely subtle Parallax Effects on Hero (max clamped roughly)
        parallaxLayers.forEach(layer => {
            const speed = parseFloat(layer.getAttribute('data-speed'));
            // limit the movement to maintain stability
            let  movement = scrollY * speed;
            if(movement > 70) movement = 70; // subtle only
            if(movement < -70) movement = -70;

            layer.style.transform = `translateY(${movement}px)`;
        });
    });

    // --- Reveal Elements on Scroll (Intersection Observer) ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2 // Trigger when element is 20% in viewport
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once revealed
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-up');
    fadeElements.forEach(el => observer.observe(el));

    // --- Horizontal Scroll Gallery Logic ---
    const track = document.getElementById('gallery-track');
    const btnPrev = document.querySelector('.nav-btn.prev');
    const btnNext = document.querySelector('.nav-btn.next');

    if (track && btnPrev && btnNext) {
        // Scroll amount is item width + gap roughly
        const scrollAmount = 450 + 32;

        btnNext.addEventListener('click', () => {
            track.parentElement.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        btnPrev.addEventListener('click', () => {
            track.parentElement.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
    }

    // --- FAQ Accordion ---
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer   = item.querySelector('.faq-answer');
        if (!question || !answer) return;

        question.addEventListener('click', () => {
            const isOpen = item.classList.contains('open');
            // Close all others
            faqItems.forEach(other => {
                other.classList.remove('open');
                other.querySelector('.faq-answer')?.classList.remove('open');
                other.querySelector('.faq-question')?.setAttribute('aria-expanded', 'false');
            });
            // Toggle clicked
            if (!isOpen) {
                item.classList.add('open');
                answer.classList.add('open');
                question.setAttribute('aria-expanded', 'true');
            }
        });
    });
    // --- Mobile Menu Toggle ---
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
            
            // Prevent scrolling when menu is open
            if (navLinks.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }
});
