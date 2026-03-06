odoo.define('zonaweb_website.main', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var _t = core._t;
    
    var ZonawebCarousel = publicWidget.Widget.extend({
        selector: '.image-carousel',
        init: function () {
            this._super.apply(this, arguments);
            this.currentSlide = 0;
            this.slides = this.$el.find('.carousel-slide');
            this.indicators = this.$el.find('.carousel-indicator');
            this.autoPlayInterval = null;
        },
        
        start: function () {
            this._super.apply(this, arguments);
            this.bindEvents();
            this.startAutoPlay();
        },
        
        bindEvents: function () {
            var self = this;
            
            // Click en indicadores
            this.indicators.on('click', function () {
                var slideIndex = parseInt($(this).data('slide'));
                self.showSlide(slideIndex);
                self.resetAutoPlay();
            });
            
            // Pausar al pasar el mouse
            this.$el.on('mouseenter', function () {
                self.stopAutoPlay();
            });
            
            this.$el.on('mouseleave', function () {
                self.startAutoPlay();
            });
        },
        
        showSlide: function (index) {
            this.slides.removeClass('active');
            this.indicators.removeClass('active');
            
            this.slides.eq(index).addClass('active');
            this.indicators.eq(index).addClass('active');
            this.currentSlide = index;
        },
        
        nextSlide: function () {
            var nextIndex = (this.currentSlide + 1) % this.slides.length;
            this.showSlide(nextIndex);
        },
        
        startAutoPlay: function () {
            var self = this;
            this.autoPlayInterval = setInterval(function () {
                self.nextSlide();
            }, 5000);
        },
        
        stopAutoPlay: function () {
            if (this.autoPlayInterval) {
                clearInterval(this.autoPlayInterval);
                this.autoPlayInterval = null;
            }
        },
        
        resetAutoPlay: function () {
            this.stopAutoPlay();
            this.startAutoPlay();
        },
        
        destroy: function () {
            this.stopAutoPlay();
            this._super.apply(this, arguments);
        }
    });
    
    publicWidget.registry.ZonawebCarousel = ZonawebCarousel;
    
    // Animaciones de scroll
    var ScrollAnimations = publicWidget.Widget.extend({
        selector: 'body',
        init: function () {
            this._super.apply(this, arguments);
            this.animatedElements = this.$('[data-animate]');
        },
        
        start: function () {
            this._super.apply(this, arguments);
            this.bindScrollEvents();
            this.checkAnimations();
        },
        
        bindScrollEvents: function () {
            var self = this;
            $(window).on('scroll', function () {
                self.checkAnimations();
            });
        },
        
        checkAnimations: function () {
            var self = this;
            var scrollTop = $(window).scrollTop();
            var windowHeight = $(window).height();
            
            this.animatedElements.each(function () {
                var $element = $(this);
                var elementTop = $element.offset().top;
                var elementHeight = $element.outerHeight();
                
                // Verificar si el elemento es visible en la pantalla
                if (scrollTop + windowHeight > elementTop + elementHeight * 0.2) {
                    if (!$element.hasClass('animated')) {
                        $element.addClass('animated');
                        var animationType = $element.data('animate') || 'fadeInUp';
                        $element.addClass('animated-' + animationType);
                    }
                }
            });
        }
    });
    
    publicWidget.registry.ScrollAnimations = ScrollAnimations;
    
    return {
        ZonawebCarousel: ZonawebCarousel,
        ScrollAnimations: ScrollAnimations
    };
});