/**
 * VAAM Import and Export Trading Co., LTD
 * Solari Template JavaScript
 */

// ============ GLOBAL VARIABLES ============
const WHATSAPP_NUMBER = '994501234567';
const COMPANY_EMAIL = 'info@vaamtrading.com';

// ============ DOM ELEMENTS ============
const mobileToggle = document.querySelector('.mobile-toggle');
const navMenu = document.querySelector('.nav-menu');
const header = document.querySelector('.header');

// ============ MOBILE MENU TOGGLE ============
if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        mobileToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });
}

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 991) {
            mobileToggle.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
});

// ============ LANGUAGE SWITCHER ============
const langBtn = document.querySelector('.lang-btn');
const langDropdown = document.querySelector('.lang-dropdown');

if (langBtn && langDropdown) {
    langBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        langBtn.classList.toggle('active');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!langBtn.contains(e.target) && !langDropdown.contains(e.target)) {
            langBtn.classList.remove('active');
        }
    });
    
    // Handle language selection
    document.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active from all options
            document.querySelectorAll('.lang-option').forEach(opt => {
                opt.classList.remove('active');
            });
            
            // Add active to clicked option
            option.classList.add('active');
            
            // Update button text
            const langText = option.textContent.trim().split(' ')[1] || option.textContent.trim();
            const langCode = option.querySelector('img').alt.substring(0, 2).toUpperCase();
            langBtn.querySelector('span').textContent = langCode;
            
            // Close dropdown
            langBtn.classList.remove('active');
            
            // Here you would typically redirect to the language version
            // For now, just show a message
            console.log('Language changed to:', langText);
            
            // Optional: Show toast notification
            // alert('Language will be: ' + langText);
        });
    });
}

// ============ STICKY HEADER ON SCROLL ============
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// ============ SCROLL ANIMATIONS (AOS) ============
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('[data-aos]');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('aos-animate');
            }
        });
    }, observerOptions);
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Initialize animations when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

// ============ COUNTER ANIMATION ============
function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000; // 2 seconds
    const step = target / (duration / 16); // 60fps
    let current = 0;
    
    const updateCounter = () => {
        current += step;
        if (current < target) {
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };
    
    updateCounter();
}

// Observe stat numbers for counter animation
const statNumbers = document.querySelectorAll('.stat-number');
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && entry.target.textContent === '0') {
            animateCounter(entry.target);
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

statNumbers.forEach(stat => statsObserver.observe(stat));

// ============ VIDEO LIGHTBOX ============
function initVideoLightbox() {
    // Create lightbox if it doesn't exist
    if (!document.querySelector('.video-lightbox')) {
        const lightbox = document.createElement('div');
        lightbox.className = 'video-lightbox';
        lightbox.innerHTML = `
            <div class="video-lightbox-content">
                <button class="video-lightbox-close">&times;</button>
                <div class="video-iframe-wrapper"></div>
            </div>
        `;
        document.body.appendChild(lightbox);
        
        // Close button
        lightbox.querySelector('.video-lightbox-close').addEventListener('click', closeVideoLightbox);
        
        // Close on background click
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeVideoLightbox();
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeVideoLightbox();
            }
        });
    }
    
    // Add click handlers to video buttons
    document.querySelectorAll('[data-video]').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const videoId = button.getAttribute('data-video');
            openVideoLightbox(videoId);
        });
    });
}

function openVideoLightbox(videoId) {
    const lightbox = document.querySelector('.video-lightbox');
    const wrapper = lightbox.querySelector('.video-iframe-wrapper');
    
    wrapper.innerHTML = `<iframe src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0" allow="autoplay; fullscreen" allowfullscreen></iframe>`;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeVideoLightbox() {
    const lightbox = document.querySelector('.video-lightbox');
    const wrapper = lightbox.querySelector('.video-iframe-wrapper');
    
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
    
    setTimeout(() => {
        wrapper.innerHTML = '';
    }, 300);
}

// Initialize video lightbox
initVideoLightbox();

// ============ SMOOTH SCROLL ============
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ============ FORM VALIDATION ============
function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function validatePhone(phone) {
    return /^[\d\s\+\-\(\)]+$/.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

function validateForm(formElement) {
    const inputs = formElement.querySelectorAll('input[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        const value = input.value.trim();
        
        if (!value) {
            showError(input, 'This field is required');
            isValid = false;
        } else if (input.type === 'email' && !validateEmail(value)) {
            showError(input, 'Please enter a valid email');
            isValid = false;
        } else if (input.type === 'tel' && !validatePhone(value)) {
            showError(input, 'Please enter a valid phone number');
            isValid = false;
        } else {
            clearError(input);
        }
    });
    
    return isValid;
}

function showError(input, message) {
    clearError(input);
    input.style.borderColor = '#f44336';
    
    const error = document.createElement('span');
    error.className = 'error-message';
    error.style.color = '#f44336';
    error.style.fontSize = '14px';
    error.style.marginTop = '5px';
    error.style.display = 'block';
    error.textContent = message;
    
    input.parentElement.appendChild(error);
}

function clearError(input) {
    input.style.borderColor = '';
    const error = input.parentElement.querySelector('.error-message');
    if (error) {
        error.remove();
    }
}

// ============ CONTACT FORMS ============
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (validateForm(this)) {
            // Get form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Create WhatsApp message
            let message = 'Hello VAAM!%0A%0A';
            Object.keys(data).forEach(key => {
                message += `${key}: ${data[key]}%0A`;
            });
            
            // Redirect to WhatsApp
            window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${message}`, '_blank');
            
            // Show success message
            alert('Thank you! Redirecting to WhatsApp...');
            this.reset();
        }
    });
});

// ============ SCROLL TO TOP BUTTON ============
function createScrollToTopButton() {
    const button = document.createElement('button');
    button.className = 'scroll-to-top';
    button.innerHTML = '<i class="fas fa-arrow-up"></i>';
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
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 998;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
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

// ============ HERO SLIDER ============
function initHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    const indicators = document.querySelectorAll('.hero-indicator');
    const prevBtn = document.querySelector('.hero-prev');
    const nextBtn = document.querySelector('.hero-next');
    
    if (!slides.length) return;
    
    let currentSlide = 0;
    const totalSlides = slides.length;
    let autoplayInterval;
    
    function showSlide(index) {
        // Remove active class from all slides and indicators
        slides.forEach(slide => {
            slide.classList.remove('active');
        });
        indicators.forEach(indicator => {
            indicator.classList.remove('active');
        });
        
        // Add active class to current slide and indicator
        slides[index].classList.add('active');
        indicators[index].classList.add('active');
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }
    
    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(currentSlide);
    }
    
    function goToSlide(index) {
        currentSlide = index;
        showSlide(currentSlide);
        resetAutoplay();
    }
    
    function startAutoplay() {
        autoplayInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
    }
    
    function stopAutoplay() {
        clearInterval(autoplayInterval);
    }
    
    function resetAutoplay() {
        stopAutoplay();
        startAutoplay();
    }
    
    // Event listeners
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetAutoplay();
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetAutoplay();
        });
    }
    
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            goToSlide(index);
        });
    });
    
    // Pause autoplay on hover
    const heroSlider = document.querySelector('.hero-slider');
    if (heroSlider) {
        heroSlider.addEventListener('mouseenter', stopAutoplay);
        heroSlider.addEventListener('mouseleave', startAutoplay);
    }
    
    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            prevSlide();
            resetAutoplay();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
            resetAutoplay();
        }
    });
    
    // Start autoplay
    startAutoplay();
}

// Initialize hero slider
initHeroSlider();

// ============ SET CURRENT YEAR ============
document.querySelectorAll('.current-year').forEach(element => {
    element.textContent = new Date().getFullYear();
});

// ============ ACTIVE PAGE HIGHLIGHTING ============
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === currentPage) {
        link.classList.add('active');
    }
});

// ============ EXPORT UTILITIES ============
window.vaamUtils = {
    validateEmail,
    validatePhone,
    validateForm,
    animateCounter
};

console.log('VAAM Website - Solari Template JS Loaded ✓');
