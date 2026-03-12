/** @odoo-module **/

document.addEventListener('DOMContentLoaded', () => {

    // ── Carousel ────────────────────────────────────────────────────────────────
    document.querySelectorAll('.image-carousel').forEach((carousel) => {
        const slides     = carousel.querySelectorAll('.carousel-slide');
        const indicators = carousel.querySelectorAll('.carousel-indicator');
        let current  = 0;
        let interval = null;

        if (!slides.length) return;

        const showSlide = (index) => {
            slides[current].classList.remove('active');
            indicators[current].classList.remove('active');
            current = index;
            slides[current].classList.add('active');
            indicators[current].classList.add('active');
        };

        const start = () => {
            interval = setInterval(() => {
                showSlide((current + 1) % slides.length);
            }, 5000);
        };

        const stop = () => {
            clearInterval(interval);
            interval = null;
        };

        indicators.forEach((indicator, i) => {
            indicator.addEventListener('click', () => {
                showSlide(i);
                stop();
                start();
            });
        });

        carousel.addEventListener('mouseenter', stop);
        carousel.addEventListener('mouseleave', start);

        start();
    });

    // ── Scroll Animations ────────────────────────────────────────────────────────
    const animatedEls = document.querySelectorAll('[data-animate]');

    const checkAnimations = () => {
        animatedEls.forEach((el) => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.85) {
                const type = el.dataset.animate || 'fadeInUp';
                el.classList.add('animated', `animated-${type}`);
            }
        });
    };

    // passive:true elimina el warning de devtools sobre scroll-blocking
    window.addEventListener('scroll', checkAnimations, { passive: true });
    checkAnimations();

});