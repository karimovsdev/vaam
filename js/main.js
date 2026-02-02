/**
 * VAAM Import and Export Trading Co., LTD
 * Main JavaScript File
 */

// ============ GLOBAL VARIABLES ============
const WHATSAPP_NUMBER = '994501234567'; // Replace with actual WhatsApp number
const COMPANY_EMAIL = 'info@vaamtrading.com';

// ============ DOM ELEMENTS ============
const mobileToggle = document.querySelector('.mobile-toggle');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');
const header = document.querySelector('.header');
const languageSwitcher = document.querySelector('.language-switcher');

// ============ MOBILE MENU TOGGLE ============
if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        mobileToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : 'auto';
    });
}

// Close mobile menu when clicking on a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
            mobileToggle.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
});

// ============ STICKY HEADER ON SCROLL ============
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// ============ ACTIVE NAVIGATION LINK ============
function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkHref = link.getAttribute('href');
        
        if (linkHref === currentPage || 
            (currentPage === '' && linkHref === 'index.html')) {
            link.classList.add('active');
        }
    });
}

// Set active link on page load
setActiveNavLink();

// ============ SMOOTH SCROLL FOR ANCHOR LINKS ============
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ============ WHATSAPP FUNCTIONS ============
function createWhatsAppLink(productName = null, message = null) {
    let text = message || `Hello VAAM! I'm interested in learning more about your solar panel products.`;
    
    if (productName) {
        text = `Hello VAAM! I'm interested in ${productName}. Please provide more details about pricing and availability.`;
    }
    
    const encodedText = encodeURIComponent(text);
    return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodedText}`;
}

function openWhatsApp(productName = null) {
    const whatsappLink = createWhatsAppLink(productName);
    window.open(whatsappLink, '_blank');
}

// Add WhatsApp click handlers to all WhatsApp buttons
document.addEventListener('DOMContentLoaded', () => {
    const whatsappButtons = document.querySelectorAll('[data-whatsapp]');
    
    whatsappButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const productName = button.getAttribute('data-product-name');
            openWhatsApp(productName);
        });
    });
});

// ============ ANIMATED COUNTERS ============
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            element.textContent = Math.round(target);
            clearInterval(timer);
        } else {
            element.textContent = Math.round(start);
        }
    }, 16);
}

// Intersection Observer for counter animation
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
            const target = parseInt(entry.target.getAttribute('data-target'));
            animateCounter(entry.target, target);
            entry.target.classList.add('counted');
        }
    });
}, observerOptions);

// Observe all counter elements
document.querySelectorAll('.stat-number[data-target]').forEach(counter => {
    counterObserver.observe(counter);
});

// ============ FADE IN ON SCROLL ANIMATION ============
const fadeElements = document.querySelectorAll('.fade-on-scroll');

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
            fadeObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

fadeElements.forEach(element => {
    fadeObserver.observe(element);
});

// ============ FORM VALIDATION ============
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^[\d\s\+\-\(\)]+$/;
    return re.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('[required]');
    
    inputs.forEach(input => {
        const errorElement = input.parentElement.querySelector('.form-error');
        
        // Remove previous error
        if (errorElement) {
            errorElement.remove();
        }
        
        input.classList.remove('error');
        
        // Check if empty
        if (!input.value.trim()) {
            showError(input, 'This field is required');
            isValid = false;
            return;
        }
        
        // Email validation
        if (input.type === 'email' && !validateEmail(input.value)) {
            showError(input, 'Please enter a valid email address');
            isValid = false;
            return;
        }
        
        // Phone validation
        if (input.type === 'tel' && !validatePhone(input.value)) {
            showError(input, 'Please enter a valid phone number');
            isValid = false;
            return;
        }
    });
    
    return isValid;
}

function showError(input, message) {
    input.classList.add('error');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-error';
    errorDiv.textContent = message;
    input.parentElement.appendChild(errorDiv);
}

function showSuccess(form, message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'form-success';
    successDiv.style.cssText = `
        background-color: #d4edda;
        color: #155724;
        padding: 16px;
        border-radius: 8px;
        margin-top: 16px;
        text-align: center;
        border: 1px solid #c3e6cb;
    `;
    successDiv.textContent = message;
    form.appendChild(successDiv);
    
    setTimeout(() => {
        successDiv.remove();
    }, 5000);
}

// Add form submit handlers
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        if (validateForm(form)) {
            // Simulate form submission
            const formData = new FormData(form);
            const data = Object.fromEntries(formData);
            
            console.log('Form submitted:', data);
            
            // Show success message
            showSuccess(form, 'Thank you! Your message has been received. We will contact you soon.');
            
            // Reset form
            form.reset();
            
            // Optional: Redirect to WhatsApp with form data
            const message = `Hello VAAM!
Name: ${data.name || 'N/A'}
Email: ${data.email || 'N/A'}
Phone: ${data.phone || 'N/A'}
Message: ${data.message || 'N/A'}`;
            
            // Uncomment to enable WhatsApp redirect after form submission
            // setTimeout(() => {
            //     window.open(createWhatsAppLink(null, message), '_blank');
            // }, 2000);
        }
    });
});

// ============ IMAGE LAZY LOADING ============
if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.dataset.src || img.src;
    });
} else {
    // Fallback for browsers that don't support lazy loading
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[loading="lazy"]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ============ LANGUAGE SWITCHER (MOBILE) ============
if (languageSwitcher && window.innerWidth <= 768) {
    const languageBtn = languageSwitcher.querySelector('.language-btn');
    
    languageBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        languageSwitcher.classList.toggle('active');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!languageSwitcher.contains(e.target)) {
            languageSwitcher.classList.remove('active');
        }
    });
}

// ============ SCROLL TO TOP ============
function createScrollToTopButton() {
    const button = document.createElement('button');
    button.className = 'scroll-to-top';
    button.innerHTML = '↑';
    button.style.cssText = `
        position: fixed;
        bottom: 100px;
        right: 30px;
        width: 50px;
        height: 50px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 50%;
        font-size: 24px;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 998;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    `;
    
    button.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            button.style.opacity = '1';
            button.style.visibility = 'visible';
        } else {
            button.style.opacity = '0';
            button.style.visibility = 'hidden';
        }
    });
    
    document.body.appendChild(button);
}

// Initialize scroll to top button
createScrollToTopButton();

// ============ UTILITIES ============
// Get current year for footer copyright
const currentYearElements = document.querySelectorAll('.current-year');
currentYearElements.forEach(element => {
    element.textContent = new Date().getFullYear();
});

// Prevent default for disabled links
document.querySelectorAll('a.disabled, .language-option.disabled').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
    });
});

// ============ EXPORT FUNCTIONS FOR USE IN OTHER FILES ============
window.vaamUtils = {
    openWhatsApp,
    createWhatsAppLink,
    validateEmail,
    validatePhone,
    validateForm,
    animateCounter
};

// ============ SCROLL ANIMATIONS (AOS-like) ============
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('[data-aos]');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('aos-animate');
                // Optionally unobserve after animation
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Initialize scroll animations when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

// ============ SMOOTH PAGE TRANSITIONS ============
function initPageTransitions() {
    // Fade in page on load
    document.body.classList.remove('page-transition');
    
    // Add transition effect when clicking internal links
    const internalLinks = document.querySelectorAll('a[href^="/"]:not([target="_blank"]), a[href$=".html"]:not([target="_blank"])');
    
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Skip if it's the current page or anchor link
            if (href === '#' || href.startsWith('#') || href === window.location.pathname) {
                return;
            }
            
            e.preventDefault();
            document.body.classList.add('page-transition');
            
            setTimeout(() => {
                window.location.href = href;
            }, 300);
        });
    });
}

// Initialize page transitions
initPageTransitions();

// ============ PARALLAX EFFECT FOR HERO SECTIONS ============
function initParallax() {
    const parallaxElements = document.querySelectorAll('[data-parallax]');
    
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        
        parallaxElements.forEach(element => {
            const speed = element.dataset.parallax || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });
}

// Initialize parallax
initParallax();

// ============ IMAGE LAZY LOADING ============
function initLazyLoading() {
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });
    
    lazyImages.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading
initLazyLoading();

// ============ VIDEO LIGHTBOX ============
function initVideoLightbox() {
    // Create lightbox HTML if it doesn't exist
    if (!document.querySelector('.video-lightbox')) {
        const lightbox = document.createElement('div');
        lightbox.className = 'video-lightbox';
        lightbox.innerHTML = `
            <div class="video-lightbox-container">
                <button class="video-lightbox-close" aria-label="Close video">&times;</button>
                <div class="video-iframe-wrapper"></div>
            </div>
        `;
        document.body.appendChild(lightbox);
        
        // Close on click outside or close button
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox || e.target.classList.contains('video-lightbox-close')) {
                closeVideoLightbox();
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && lightbox.classList.contains('active')) {
                closeVideoLightbox();
            }
        });
    }
    
    // Add click handlers to video play buttons
    const videoButtons = document.querySelectorAll('[data-video]');
    videoButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const videoId = this.dataset.video;
            const videoType = this.dataset.videoType || 'youtube'; // youtube or vimeo
            openVideoLightbox(videoId, videoType);
        });
    });
}

function openVideoLightbox(videoId, type = 'youtube') {
    const lightbox = document.querySelector('.video-lightbox');
    const wrapper = lightbox.querySelector('.video-iframe-wrapper');
    
    let embedUrl = '';
    if (type === 'youtube') {
        embedUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;
    } else if (type === 'vimeo') {
        embedUrl = `https://player.vimeo.com/video/${videoId}?autoplay=1`;
    }
    
    wrapper.innerHTML = `<iframe src="${embedUrl}" allow="autoplay; fullscreen" allowfullscreen></iframe>`;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeVideoLightbox() {
    const lightbox = document.querySelector('.video-lightbox');
    const wrapper = lightbox.querySelector('.video-iframe-wrapper');
    
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
    
    // Stop video by removing iframe
    setTimeout(() => {
        wrapper.innerHTML = '';
    }, 300);
}

// Initialize video lightbox
initVideoLightbox();

console.log('VAAM Website - Main JS Loaded Successfully ✓');
