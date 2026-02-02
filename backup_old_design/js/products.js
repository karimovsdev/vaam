/**
 * VAAM - Products Catalog JavaScript
 * Handles product filtering, sorting, and display
 */

// ============ PRODUCT DATA ============
const products = [
    {
        id: 'VAAM-M-400',
        name: 'VAAM Monocrystalline 400W',
        category: 'Monocrystalline',
        power: 400,
        efficiency: 20.5,
        dimensions: '1722×1134×30mm',
        weight: '22kg',
        price: 120,
        warranty: '25 years',
        features: [
            'High efficiency mono PERC cells',
            'Excellent low light performance',
            'Resistant to harsh weather',
            'Positive power tolerance'
        ],
        image: 'https://images.unsplash.com/photo-1509391366360-2e959784a276?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-M-550',
        name: 'VAAM Bifacial 550W Module',
        category: 'Bifacial',
        power: 550,
        efficiency: 21.2,
        dimensions: '2278×1134×35mm',
        weight: '29kg',
        price: 165,
        warranty: '25 years',
        features: [
            'Bifacial technology for higher yield',
            'Industry-leading efficiency',
            'Dual glass construction',
            'Superior performance in all conditions'
        ],
        image: 'https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-P-350',
        name: 'VAAM Polycrystalline 350W',
        category: 'Polycrystalline',
        power: 350,
        efficiency: 18.8,
        dimensions: '1722×1134×35mm',
        weight: '21kg',
        price: 95,
        warranty: '20 years',
        features: [
            'Cost-effective solution',
            'Reliable performance',
            'Proven technology',
            'Suitable for various applications'
        ],
        image: 'https://images.unsplash.com/photo-1559302504-64aae6ca6b6d?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-M-450',
        name: 'VAAM Monocrystalline 450W',
        category: 'Monocrystalline',
        power: 450,
        efficiency: 21.0,
        dimensions: '1909×1134×30mm',
        weight: '24kg',
        price: 135,
        warranty: '25 years',
        features: [
            'Half-cut cell technology',
            'Reduced hot spot temperature',
            'Better shade tolerance',
            'Enhanced mechanical load capacity'
        ],
        image: 'https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-TF-300',
        name: 'VAAM Thin-Film 300W Panel',
        category: 'Thin-Film',
        power: 300,
        efficiency: 16.5,
        dimensions: '1956×1310×35mm',
        weight: '26kg',
        price: 85,
        warranty: '15 years',
        features: [
            'Excellent temperature coefficient',
            'Better low-light performance',
            'Flexible mounting options',
            'Aesthetic appearance'
        ],
        image: 'https://images.unsplash.com/photo-1497440001374-f26997328c1b?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-M-500',
        name: 'VAAM High Power 500W Module',
        category: 'Monocrystalline',
        power: 500,
        efficiency: 21.5,
        dimensions: '2094×1134×35mm',
        weight: '27kg',
        price: 155,
        warranty: '25 years',
        features: [
            'Maximum power output',
            'Industry-leading warranty',
            'Superior quality materials',
            'Certified for global standards'
        ],
        image: 'https://images.unsplash.com/photo-1559302504-70e3b11b3711?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-CS-5000',
        name: 'VAAM Commercial System 5kW',
        category: 'Commercial',
        power: 5000,
        efficiency: 20.8,
        dimensions: 'Complete System',
        weight: 'System',
        price: 4500,
        warranty: '25 years',
        features: [
            'Complete commercial solution',
            'Grid-tied inverter included',
            'Monitoring system',
            'Professional installation support'
        ],
        image: 'https://images.unsplash.com/photo-1611365892117-00ac5ef43c90?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-RS-3000',
        name: 'VAAM Residential Kit 3kW',
        category: 'Residential',
        power: 3000,
        efficiency: 20.2,
        dimensions: 'Complete Kit',
        weight: 'System',
        price: 2800,
        warranty: '25 years',
        features: [
            'Perfect for homes',
            'Easy installation',
            'Complete package with inverter',
            'Mobile app monitoring'
        ],
        image: 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-B-600',
        name: 'VAAM Bifacial Premium 600W',
        category: 'Bifacial',
        power: 600,
        efficiency: 21.8,
        dimensions: '2384×1303×35mm',
        weight: '32kg',
        price: 190,
        warranty: '30 years',
        features: [
            'Premium efficiency rating',
            'Extended warranty',
            'Optimized for all climates',
            'Industry-leading performance'
        ],
        image: 'https://images.unsplash.com/photo-1624397640148-949b1732bb0a?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-P-380',
        name: 'VAAM Polycrystalline 380W',
        category: 'Polycrystalline',
        power: 380,
        efficiency: 19.2,
        dimensions: '1956×992×40mm',
        weight: '23kg',
        price: 105,
        warranty: '20 years',
        features: [
            'Great value for money',
            'Reliable power generation',
            'Proven durability',
            'Wide temperature range'
        ],
        image: 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-CS-10000',
        name: 'VAAM Commercial System 10kW',
        category: 'Commercial',
        power: 10000,
        efficiency: 21.0,
        dimensions: 'Complete System',
        weight: 'System',
        price: 8500,
        warranty: '25 years',
        features: [
            'Large-scale commercial solution',
            'Three-phase inverter',
            'Advanced monitoring',
            'ROI optimization'
        ],
        image: 'https://images.unsplash.com/photo-1532601224476-15c79f2f7a51?w=400&h=300&fit=crop'
    },
    {
        id: 'VAAM-RS-5000',
        name: 'VAAM Residential Premium 5kW',
        category: 'Residential',
        power: 5000,
        efficiency: 21.2,
        dimensions: 'Complete Kit',
        weight: 'System',
        price: 4200,
        warranty: '25 years',
        features: [
            'Premium home solution',
            'Battery ready system',
            'Smart energy management',
            'Backup power capability'
        ],
        image: 'https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6?w=400&h=300&fit=crop'
    }
];

// ============ FILTER & SORT STATE ============
let currentCategory = 'all';
let currentPriceRange = 'all';
let currentPowerRange = 'all';
let currentSort = 'default';

// ============ RENDER PRODUCTS ============
function renderProducts(productsToRender) {
    const productsContainer = document.getElementById('products-container');
    
    if (!productsContainer) return;
    
    productsContainer.innerHTML = '';
    
    if (productsToRender.length === 0) {
        productsContainer.innerHTML = `
            <div class="no-products">
                <p>No products found matching your criteria.</p>
            </div>
        `;
        return;
    }
    
    productsToRender.forEach(product => {
        const productCard = createProductCard(product);
        productsContainer.appendChild(productCard);
    });
    
    // Update results count
    const resultsCount = document.getElementById('results-count');
    if (resultsCount) {
        resultsCount.textContent = `Showing ${productsToRender.length} product${productsToRender.length !== 1 ? 's' : ''}`;
    }
}

// ============ CREATE PRODUCT CARD ============
function createProductCard(product) {
    const card = document.createElement('div');
    card.className = 'card product-card fade-on-scroll';
    
    card.innerHTML = `
        <div style="position: relative;">
            <img src="${product.image}" alt="${product.name}" class="product-image" loading="lazy">
            ${product.efficiency >= 21 ? '<span class="product-badge">High Efficiency</span>' : ''}
        </div>
        <div class="product-body">
            <div class="product-category">${product.category}</div>
            <h3 class="product-title">${product.name}</h3>
            <div class="product-specs">
                <span class="product-spec"><strong>Power:</strong> ${product.power}W</span>
                <span class="product-spec"><strong>Efficiency:</strong> ${product.efficiency}%</span>
            </div>
            <div class="product-specs">
                <span class="product-spec"><strong>Size:</strong> ${product.dimensions}</span>
                <span class="product-spec"><strong>Warranty:</strong> ${product.warranty}</span>
            </div>
            <ul style="list-style: disc; padding-left: 20px; margin: 16px 0; color: #666;">
                ${product.features.slice(0, 2).map(feature => `<li>${feature}</li>`).join('')}
            </ul>
            <div class="product-price">
                $${product.price.toLocaleString()}
                <span class="product-price-currency">USD</span>
            </div>
            <button class="btn btn-whatsapp" data-whatsapp data-product-name="${product.name}" style="width: 100%;">
                <span>💬</span> Inquire on WhatsApp
            </button>
        </div>
    `;
    
    // Add WhatsApp event listener
    const whatsappBtn = card.querySelector('[data-whatsapp]');
    whatsappBtn.addEventListener('click', () => {
        window.vaamUtils.openWhatsApp(product.name);
    });
    
    return card;
}

// ============ FILTER PRODUCTS ============
function filterProducts() {
    let filtered = [...products];
    
    // Filter by category
    if (currentCategory !== 'all') {
        filtered = filtered.filter(p => p.category === currentCategory);
    }
    
    // Filter by price range
    if (currentPriceRange !== 'all') {
        const [min, max] = currentPriceRange.split('-').map(Number);
        if (max) {
            filtered = filtered.filter(p => p.price >= min && p.price <= max);
        } else {
            filtered = filtered.filter(p => p.price >= min);
        }
    }
    
    // Filter by power range
    if (currentPowerRange !== 'all') {
        const [min, max] = currentPowerRange.split('-').map(Number);
        if (max) {
            filtered = filtered.filter(p => p.power >= min && p.power <= max);
        } else {
            filtered = filtered.filter(p => p.power >= min);
        }
    }
    
    // Sort products
    sortProducts(filtered);
    
    renderProducts(filtered);
    
    // Re-observe fade elements
    document.querySelectorAll('.fade-on-scroll').forEach(element => {
        const fadeObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                }
            });
        }, { threshold: 0.1 });
        fadeObserver.observe(element);
    });
}

// ============ SORT PRODUCTS ============
function sortProducts(productsArray) {
    switch (currentSort) {
        case 'price-low':
            productsArray.sort((a, b) => a.price - b.price);
            break;
        case 'price-high':
            productsArray.sort((a, b) => b.price - a.price);
            break;
        case 'power-low':
            productsArray.sort((a, b) => a.power - b.power);
            break;
        case 'power-high':
            productsArray.sort((a, b) => b.power - a.power);
            break;
        case 'efficiency':
            productsArray.sort((a, b) => b.efficiency - a.efficiency);
            break;
        default:
            // Default order (as defined in data)
            break;
    }
}

// ============ SEARCH PRODUCTS ============
function searchProducts(query) {
    if (!query) {
        filterProducts();
        return;
    }
    
    const searchTerm = query.toLowerCase();
    const filtered = products.filter(product => {
        return (
            product.name.toLowerCase().includes(searchTerm) ||
            product.category.toLowerCase().includes(searchTerm) ||
            product.features.some(feature => feature.toLowerCase().includes(searchTerm))
        );
    });
    
    renderProducts(filtered);
}

// ============ EVENT LISTENERS ============
document.addEventListener('DOMContentLoaded', () => {
    // Category filter
    const categoryButtons = document.querySelectorAll('[data-category]');
    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentCategory = button.getAttribute('data-category');
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            filterProducts();
        });
    });
    
    // Price range filter
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', (e) => {
            currentPriceRange = e.target.value;
            filterProducts();
        });
    }
    
    // Power range filter
    const powerFilter = document.getElementById('power-filter');
    if (powerFilter) {
        powerFilter.addEventListener('change', (e) => {
            currentPowerRange = e.target.value;
            filterProducts();
        });
    }
    
    // Sort dropdown
    const sortFilter = document.getElementById('sort-filter');
    if (sortFilter) {
        sortFilter.addEventListener('change', (e) => {
            currentSort = e.target.value;
            filterProducts();
        });
    }
    
    // Search input
    const searchInput = document.getElementById('product-search');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                searchProducts(e.target.value);
            }, 300);
        });
    }
    
    // Reset filters button
    const resetButton = document.getElementById('reset-filters');
    if (resetButton) {
        resetButton.addEventListener('click', () => {
            currentCategory = 'all';
            currentPriceRange = 'all';
            currentPowerRange = 'all';
            currentSort = 'default';
            
            // Reset UI
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            document.querySelector('[data-category="all"]')?.classList.add('active');
            if (priceFilter) priceFilter.value = 'all';
            if (powerFilter) powerFilter.value = 'all';
            if (sortFilter) sortFilter.value = 'default';
            if (searchInput) searchInput.value = '';
            
            filterProducts();
        });
    }
    
    // Initial render
    renderProducts(products);
});

// ============ EXPORT FOR EXTERNAL USE ============
window.vaamProducts = {
    products,
    filterProducts,
    searchProducts,
    renderProducts
};

console.log('VAAM Products - Catalog JS Loaded Successfully ✓');
