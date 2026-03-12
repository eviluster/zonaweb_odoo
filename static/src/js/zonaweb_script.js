/** @odoo-module **/

document.addEventListener('DOMContentLoaded', () => {

    // ── Carousel del hero ──────────────────────────
    const slides = document.querySelectorAll('.zw-carousel-slide');
    const dots   = document.querySelectorAll('.zw-carousel-dot');
    if (slides.length) {
        let current = 0;
        const goTo = (idx) => {
            slides[current].classList.remove('active');
            dots[current] && dots[current].classList.remove('active');
            current = (idx + slides.length) % slides.length;
            slides[current].classList.add('active');
            dots[current] && dots[current].classList.add('active');
        };
        dots.forEach((dot, i) => dot.addEventListener('click', () => goTo(i)));
        setInterval(() => goTo(current + 1), 4500);
    }

    // ── Scroll reveal ──────────────────────────────
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.zw-service-card, .zw-portfolio-card, .zw-pf-card, .zw-plan-card, .zw-team-card').forEach((el, i) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(24px)';
        el.style.transition = `opacity 0.5s ease ${i * 0.08}s, transform 0.5s ease ${i * 0.08}s`;
        observer.observe(el);
    });

    // ── Filtros del portafolio ─────────────────────
    const filterBtns = document.querySelectorAll('.zw-filter-btn');
    const pfCards    = document.querySelectorAll('.zw-pf-card[data-cat]');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const cat = btn.dataset.filter;
            pfCards.forEach(card => {
                const show = cat === 'all' || card.dataset.cat === cat;
                card.style.display = show ? 'block' : 'none';
            });
        });
    });

    // ── Smooth scroll ──────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', (e) => {
            const target = document.querySelector(a.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ── Contadores animados ────────────────────────
    const counters = document.querySelectorAll('[data-count]');
    const countObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el  = entry.target;
                const end = parseInt(el.dataset.count, 10);
                const duration = 1800;
                const step = Math.ceil(end / (duration / 16));
                let current = 0;
                const timer = setInterval(() => {
                    current = Math.min(current + step, end);
                    el.textContent = current;
                    if (current >= end) clearInterval(timer);
                }, 16);
                countObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });
    counters.forEach(c => countObserver.observe(c));

    // ── Navbar scroll shadow ───────────────────────
    const navbar = document.querySelector('.o_main_navbar, nav.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            navbar.style.boxShadow = window.scrollY > 20
                ? '0 4px 20px rgba(11,31,58,0.15)'
                : '';
        }, { passive: true });
    }

});