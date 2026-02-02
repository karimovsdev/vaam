# VAAM Website - Image Requirements

## Directory Structure
```
images/
├── logo/
│   └── vaam-logo.png (Required - Company logo)
├── hero/
│   ├── hero-bg-1.jpg (1920x1080px)
│   ├── hero-bg-2.jpg (1920x1080px)
│   └── hero-bg-3.jpg (1920x1080px)
├── about/
│   ├── company.jpg (800x600px)
│   ├── team.jpg (800x600px)
│   └── certifications/ (Certificate images)
├── products/
│   └── (12 product images - already referenced in products.js)
├── services/
│   ├── installation.jpg (600x400px)
│   ├── maintenance.jpg (600x400px)
│   ├── consultation.jpg (600x400px)
│   ├── monitoring.jpg (600x400px)
│   ├── warranty.jpg (600x400px)
│   └── financing.jpg (600x400px)
├── projects/
│   └── (Project portfolio images)
├── news/
│   └── (Blog/news images)
├── testimonials/
│   ├── client-1.jpg (150x150px)
│   ├── client-2.jpg (150x150px)
│   └── client-3.jpg (150x150px)
├── steps/
│   ├── step-1.png (Icon/illustration)
│   ├── step-2.png (Icon/illustration)
│   └── step-3.png (Icon/illustration)
├── faq/
│   └── faq-image.jpg (600x400px)
├── brands/
│   └── (Partner/brand logos)
└── icons/
    └── (Various UI icons)
```

## Image Sources

### Option 1: Use Placeholder Services (Temporary)
- **Unsplash**: https://source.unsplash.com/1920x1080/?solar,panel
- **Placeholder.com**: https://via.placeholder.com/800x600
- **Lorem Picsum**: https://picsum.photos/800/600

### Option 2: Professional Stock Photos
- Unsplash.com (free)
- Pexels.com (free)
- Freepik.com (free with attribution)

### Option 3: Custom Photography
- Hire professional photographer
- Use company's actual projects and facilities

## Priority Images

### Critical (Website won't look complete without these):
1. **vaam-logo.png** - Company logo (transparent PNG)
2. **hero-bg-1.jpg** - Main hero background
3. **Product images** - Referenced in products.js

### High Priority:
4. Services images (6 images)
5. About company image
6. Project portfolio images (6-12 images)

### Medium Priority:
7. Testimonial client photos
8. News/blog images
9. Partner brand logos

### Low Priority (Can use icons/illustrations):
10. Step/process icons
11. FAQ imagery
12. Decorative elements

## Image Specifications

### Format:
- **Photos**: JPG (optimized, 80-85% quality)
- **Logos/Icons**: PNG (transparent background)
- **Illustrations**: SVG (preferred) or PNG

### Optimization:
- Compress all images before upload
- Use WebP format for modern browsers
- Implement lazy loading (already in code)

### Dimensions:
- Hero images: 1920x1080px (Full HD)
- Service cards: 600x400px
- Product images: 400x300px
- Thumbnails: 150x150px

## Temporary Solution

Until you have actual images, the website uses:
1. CSS background gradients for hero sections
2. Placeholder image services with solar panel keywords
3. Icon fonts and emojis for decorative elements
4. CSS-based loading states

## Next Steps

1. Add **vaam-logo.png** to `images/logo/` directory
2. Update product images in `images/products/`
3. Add hero backgrounds in `images/hero/`
4. Gradually replace placeholders with actual photos
