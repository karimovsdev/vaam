/**
 * VAAM Import and Export Trading Co., LTD
 * Alpine.js + Tailwind CSS Application
 */

// ============ ALPINE.JS GLOBAL STORE ============
document.addEventListener('alpine:init', () => {
    // Global Store
    Alpine.store('app', {
        whatsappNumber: '994501234567',
        companyEmail: 'info@vaamtrading.com',
        currentYear: new Date().getFullYear(),
    });

    // Navigation Component
    Alpine.data('navbar', () => ({
        mobileOpen: false,
        scrolled: false,
        langOpen: false,

        init() {
            window.addEventListener('scroll', () => {
                this.scrolled = window.scrollY > 80;
            });
        },

        toggleMobile() {
            this.mobileOpen = !this.mobileOpen;
            document.body.style.overflow = this.mobileOpen ? 'hidden' : 'auto';
        },

        closeMobile() {
            this.mobileOpen = false;
            document.body.style.overflow = 'auto';
        },

        isActive(page) {
            const current = window.location.pathname.split('/').pop() || 'index.html';
            return current === page || (current === '' && page === 'index.html');
        }
    }));

    // Hero Slider Component - defined inline in home.html template for Django data access

    // Counter Animation Component
    Alpine.data('counter', () => ({
        count: 0,
        target: 0,
        animated: false,

        init() {
            this.target = parseInt(this.$el.dataset.target) || 0;
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !this.animated) {
                        this.animated = true;
                        this.animateCount();
                    }
                });
            }, { threshold: 0.5 });

            observer.observe(this.$el);
        },

        animateCount() {
            const duration = 2000;
            const steps = 60;
            const increment = this.target / steps;
            let current = 0;
            const stepTime = duration / steps;

            const timer = setInterval(() => {
                current += increment;
                if (current >= this.target) {
                    this.count = this.target;
                    clearInterval(timer);
                } else {
                    this.count = Math.round(current);
                }
            }, stepTime);
        }
    }));

    // Scroll Animation Component
    Alpine.data('scrollAnimate', () => ({
        visible: false,

        init() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            this.visible = true;
                        }, parseInt(this.$el.dataset.delay || 0));
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

            observer.observe(this.$el);
        }
    }));

    // Project Filter Component
    Alpine.data('projectFilter', () => ({
        activeFilter: 'all',

        setFilter(filter) {
            this.activeFilter = filter;
        },

        isVisible(category) {
            return this.activeFilter === 'all' || this.activeFilter === category;
        }
    }));

    // Contact Form Component
    Alpine.data('contactForm', () => ({
        formData: {
            name: '',
            email: '',
            phone: '',
            company: '',
            subject: '',
            message: ''
        },
        errors: {},
        submitted: false,
        loading: false,

        validateEmail(email) {
            return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
        },

        validatePhone(phone) {
            return /^[\d\s\+\-\(\)]+$/.test(phone) && phone.replace(/\D/g, '').length >= 10;
        },

        validate() {
            this.errors = {};
            
            if (!this.formData.name.trim()) this.errors.name = 'Name is required';
            if (!this.formData.email.trim()) this.errors.email = 'Email is required';
            else if (!this.validateEmail(this.formData.email)) this.errors.email = 'Invalid email format';
            if (!this.formData.phone.trim()) this.errors.phone = 'Phone is required';
            else if (!this.validatePhone(this.formData.phone)) this.errors.phone = 'Invalid phone number';
            if (!this.formData.subject) this.errors.subject = 'Subject is required';
            if (!this.formData.message.trim()) this.errors.message = 'Message is required';

            return Object.keys(this.errors).length === 0;
        },

        submit() {
            if (!this.validate()) return;

            this.loading = true;

            // Build WhatsApp message
            let msg = `Hello VAAM!%0A%0A`;
            msg += `*New Contact Form*%0A%0A`;
            msg += `*Name:* ${this.formData.name}%0A`;
            msg += `*Email:* ${this.formData.email}%0A`;
            msg += `*Phone:* ${this.formData.phone}%0A`;
            if (this.formData.company) msg += `*Company:* ${this.formData.company}%0A`;
            msg += `*Subject:* ${this.formData.subject}%0A%0A`;
            msg += `*Message:*%0A${this.formData.message}`;

            window.open(`https://wa.me/${Alpine.store('app').whatsappNumber}?text=${msg}`, '_blank');

            this.submitted = true;
            this.loading = false;
            this.formData = { name: '', email: '', phone: '', company: '', subject: '', message: '' };

            setTimeout(() => {
                this.submitted = false;
            }, 5000);
        }
    }));

    // Video Lightbox Component
    Alpine.data('videoLightbox', () => ({
        open: false,
        videoId: '',

        openVideo(id) {
            this.videoId = id;
            this.open = true;
            document.body.style.overflow = 'hidden';
        },

        closeVideo() {
            this.open = false;
            this.videoId = '';
            document.body.style.overflow = 'auto';
        }
    }));
});

// ============ SCROLL TO TOP ============
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
            }
        });
    });
});

// ============ WHATSAPP HELPER ============
function openWhatsApp(productName = null) {
    const number = '994501234567';
    let text = productName
        ? `Hello VAAM! I'm interested in ${productName}. Please provide more details.`
        : `Hello VAAM! I'm interested in your solar panel products.`;
    window.open(`https://wa.me/${number}?text=${encodeURIComponent(text)}`, '_blank');
}

console.log('VAAM Website - Alpine.js + Tailwind CSS Loaded ✓');
