/** @odoo-module **/

import { registry } from "@web/core/registry";
import publicWidget from "@website/js/public.widget";

// ─── Carousel Widget ───────────────────────────────────────────────────────────
const ZonawebCarousel = publicWidget.Widget.extend({
    selector: '.image-carousel',

    start() {
        this._super(...arguments);
        this.currentSlide = 0;
        this.slides = this.el.querySelectorAll('.carousel-slide');
        this.indicators = this.el.querySelectorAll('.carousel-indicator');
        this.autoPlayInterval = null;
        this._bindEvents();
        this._startAutoPlay();
        return Promise.resolve();
    },

    _bindEvents() {
        this.indicators.forEach((indicator) => {
            indicator.addEventListener('click', () => {
                const index = parseInt(indicator.dataset.slide);
                this._showSlide(index);
                this._resetAutoPlay();
            });
        });

        this.el.addEventListener('mouseenter', () => this._stopAutoPlay());
        this.el.addEventListener('mouseleave', () => this._startAutoPlay());
    },

    _showSlide(index) {
        this.slides.forEach(s => s.classList.remove('active'));
        this.indicators.forEach(i => i.classList.remove('active'));
        this.slides[index].classList.add('active');
        this.indicators[index].classList.add('active');
        this.currentSlide = index;
    },

    _nextSlide() {
        this._showSlide((this.currentSlide + 1) % this.slides.length);
    },

    _startAutoPlay() {
        this.autoPlayInterval = setInterval(() => this._nextSlide(), 5000);
    },

    _stopAutoPlay() {
        if (this.autoPlayInterval) {
            clearInterval(this.autoPlayInterval);
            this.autoPlayInterval = null;
        }
    },

    _resetAutoPlay() {
        this._stopAutoPlay();
        this._startAutoPlay();
    },

    destroy() {
        this._stopAutoPlay();
        this._super(...arguments);
    },
});

publicWidget.registry.ZonawebCarousel = ZonawebCarousel;


// ─── Scroll Animations Widget ──────────────────────────────────────────────────
const ScrollAnimations = publicWidget.Widget.extend({
    selector: 'body',

    start() {
        this._super(...arguments);
        this.animatedElements = this.el.querySelectorAll('[data-animate]');
        this._bindScrollEvents();
        this._checkAnimations();
        return Promise.resolve();
    },

    _bindScrollEvents() {
        this._onScroll = () => this._checkAnimations();
        window.addEventListener('scroll', this._onScroll);
    },

    _checkAnimations() {
        const scrollTop = window.scrollY;
        const windowHeight = window.innerHeight;

        this.animatedElements.forEach((el) => {
            const rect = el.getBoundingClientRect();
            const elementTop = rect.top + scrollTop;

            if (scrollTop + windowHeight > elementTop + rect.height * 0.2) {
                if (!el.classList.contains('animated')) {
                    const animationType = el.dataset.animate || 'fadeInUp';
                    el.classList.add('animated', `animated-${animationType}`);
                }
            }
        });
    },

    destroy() {
        window.removeEventListener('scroll', this._onScroll);
        this._super(...arguments);
    },
});

publicWidget.registry.ScrollAnimations = ScrollAnimations;