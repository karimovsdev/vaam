/**
 * VAAM Products Page - Dynamic Product Loading and Filtering
 */

let allProducts = [];
let filteredProducts = [];

// Load products from JSON
async function loadProducts() {
    try {
        const response = await fetch('assets/data/products.json');
        const data = await response.json();
        allProducts = data.products;
        filteredProducts = [...allProducts];
        renderProducts();
    } catch (error) {
        console.error('Error loading products:', error);
        document.getElementById('productsGrid').innerHTML = `
            <div class="error-message">
                <i class="fas fa-exclamation-triangle"></i>
                <p>Failed to load products. Please try again later.</p>
            </div>
        `;
    }
}

// Render products to grid
function renderProducts() {
    const grid = document.getElementById('productsGrid');
    
    if (filteredProducts.length === 0) {
        grid.innerHTML = `
            <div class="no-results">
                <i class="fas fa-search"></i>
                <p>No products found matching your criteria.</p>
            </div>
        `;
        return;
    }
    
    grid.innerHTML = filteredProducts.map(product => `
        <div class="product-card" data-aos="fade-up">
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}">
                <span class="product-badge">${product.category}</span>
            </div>
            <div class="product-content">
                <h3 class="product-name">${product.name}</h3>
                <div class="product-specs">
                    <div class="spec-item">
                        <i class="fas fa-bolt"></i>
                        <span>${product.power >= 1000 ? (product.power / 1000) + 'kW' : product.power + 'W'}</span>
                    </div>
                    <div class="spec-item">
                        <i class="fas fa-chart-line"></i>
                        <span>${product.efficiency}%</span>
                    </div>
                    <div class="spec-item">
                        <i class="fas fa-ruler-combined"></i>
                        <span>${product.dimensions}</span>
                    </div>
                </div>
                <ul class="product-features">
                    ${product.features.slice(0, 3).map(feature => `
                        <li><i class="fas fa-check"></i> ${feature}</li>
                    `).join('')}
                </ul>
                <div class="product-footer">
                    <div class="product-price">
                        <span class="price">${product.currency} $${product.price.toLocaleString()}</span>
                        <span class="warranty"><i class="fas fa-shield-alt"></i> ${product.warranty}</span>
                    </div>
                    <a href="https://wa.me/994501234567?text=${encodeURIComponent(product.whatsappMessage)}" 
                       class="btn btn-primary btn-sm"
                       target="_blank">
                        <i class="fab fa-whatsapp"></i> Inquire
                    </a>
                </div>
            </div>
        </div>
    `).join('');
}

// Filter products
function filterProducts() {
    const category = document.getElementById('categoryFilter').value;
    const powerRange = document.getElementById('powerFilter').value;
    
    filteredProducts = allProducts.filter(product => {
        // Category filter
        if (category !== 'all' && product.category !== category) {
            return false;
        }
        
        // Power filter
        if (powerRange !== 'all') {
            const [min, max] = powerRange.split('-').map(Number);
            if (product.power < min || product.power > max) {
                return false;
            }
        }
        
        return true;
    });
    
    sortProducts();
}

// Sort products
function sortProducts() {
    const sortBy = document.getElementById('sortFilter').value;
    
    switch (sortBy) {
        case 'price-low':
            filteredProducts.sort((a, b) => a.price - b.price);
            break;
        case 'price-high':
            filteredProducts.sort((a, b) => b.price - a.price);
            break;
        case 'power-low':
            filteredProducts.sort((a, b) => a.power - b.power);
            break;
        case 'power-high':
            filteredProducts.sort((a, b) => b.power - a.power);
            break;
        case 'efficiency':
            filteredProducts.sort((a, b) => b.efficiency - a.efficiency);
            break;
        default:
            // Keep default order
            break;
    }
    
    renderProducts();
}

// Add event listeners
document.addEventListener('DOMContentLoaded', () => {
    loadProducts();
    
    document.getElementById('categoryFilter').addEventListener('change', filterProducts);
    document.getElementById('powerFilter').addEventListener('change', filterProducts);
    document.getElementById('sortFilter').addEventListener('change', sortProducts);
});
