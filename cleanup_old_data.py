"""
VAAM - Cleanup Old Demo/Test Data
This script removes old demo/test data while preserving the real client data
Run: python cleanup_old_data.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from core.models import (
    HeroSlide, News, NewsCategory, Product, ProductCategory, ProductImage, ProductSpecification,
    Service, ServiceCategory, Project, ProjectCategory, ProjectImage,
    Brand, Testimonial, Certificate, TeamMember, CompanyFeature, Statistic, ProcessStep, FAQ
)

print("=" * 80)
print("  VAAM - Cleaning Up Old Demo/Test Data")
print("=" * 80)
print("\nThis will remove old demo data while keeping the new client data.")
print("Real client data identifiers:")
print("  - Hero: 'Your Reliable Trading Partner in China'")
print("  - News: 'New Street and Garden Lighting Projects'")
print("  - Features: 6 items about company strengths")
print("  - Statistics: 5 items (50+, 30+, 1+, 5 MW+, 3+)")
print("  - Product Categories: 6 items")
print("  - Process Steps: 6 items")
print("  - FAQs: 8 items")
print("\n" + "=" * 80)

# Track deletions
deleted_count = {}

# 1. HERO SLIDES - Keep only real client slide
print("\n[1/13] Cleaning Hero Slides...")
old_hero_slides = HeroSlide.objects.exclude(title_en__icontains="Reliable Trading Partner")
count = old_hero_slides.count()
if count > 0:
    old_hero_slides.delete()
    deleted_count['HeroSlide'] = count
    print(f"   ✓ Deleted {count} old hero slides")
else:
    print(f"   ✓ No old hero slides to delete")

# 2. NEWS - Keep only real client news
print("\n[2/13] Cleaning News...")
old_news = News.objects.exclude(slug="new-street-garden-lighting-projects")
count = old_news.count()
if count > 0:
    old_news.delete()
    deleted_count['News'] = count
    print(f"   ✓ Deleted {count} old news articles")
else:
    print(f"   ✓ No old news to delete")

# 3. NEWS CATEGORIES - Keep only Company News
print("\n[3/13] Cleaning News Categories...")
NewsCategory.objects.exclude(slug="company-news").delete()
print(f"   ✓ Cleaned news categories")

# 4. PRODUCTS - Delete all demo products
print("\n[4/13] Cleaning Products...")
count = Product.objects.count()
if count > 0:
    ProductImage.objects.all().delete()
    ProductSpecification.objects.all().delete()
    Product.objects.all().delete()
    deleted_count['Product'] = count
    print(f"   ✓ Deleted {count} demo products (real products will be added later)")
else:
    print(f"   ✓ No products to delete")

# 5. PRODUCT CATEGORIES - Keep only the 6 real ones we added
print("\n[5/13] Checking Product Categories...")
real_categories = ['solar-panels', 'street-garden-lighting', 'security-cameras', 
                   'automobiles', 'construction-materials', 'industrial-products']
old_categories = ProductCategory.objects.exclude(slug__in=real_categories)
count = old_categories.count()
if count > 0:
    old_categories.delete()
    deleted_count['ProductCategory'] = count
    print(f"   ✓ Deleted {count} old product categories")
else:
    print(f"   ✓ All product categories are correct")

# 6. SERVICES - Delete all demo services
print("\n[6/13] Cleaning Services...")
count = Service.objects.count()
if count > 0:
    Service.objects.all().delete()
    deleted_count['Service'] = count
    print(f"   ✓ Deleted {count} demo services (real services will be added later)")
else:
    print(f"   ✓ No services to delete")

# 7. SERVICE CATEGORIES
print("\n[7/13] Cleaning Service Categories...")
ServiceCategory.objects.all().delete()
print(f"   ✓ Cleaned service categories")

# 8. PROJECTS - Delete all demo projects
print("\n[8/13] Cleaning Projects...")
count = Project.objects.count()
if count > 0:
    ProjectImage.objects.all().delete()
    Project.objects.all().delete()
    deleted_count['Project'] = count
    print(f"   ✓ Deleted {count} demo projects (real projects will be added later)")
else:
    print(f"   ✓ No projects to delete")

# 9. PROJECT CATEGORIES
print("\n[9/13] Cleaning Project Categories...")
ProjectCategory.objects.all().delete()
print(f"   ✓ Cleaned project categories")

# 10. BRANDS/PARTNERS - Delete all demo brands
print("\n[10/13] Cleaning Brands/Partners...")
count = Brand.objects.count()
if count > 0:
    Brand.objects.all().delete()
    deleted_count['Brand'] = count
    print(f"   ✓ Deleted {count} demo brands")
else:
    print(f"   ✓ No brands to delete")

# 11. TESTIMONIALS - Delete all demo testimonials
print("\n[11/13] Cleaning Testimonials...")
count = Testimonial.objects.count()
if count > 0:
    Testimonial.objects.all().delete()
    deleted_count['Testimonial'] = count
    print(f"   ✓ Deleted {count} demo testimonials")
else:
    print(f"   ✓ No testimonials to delete")

# 12. TEAM MEMBERS - Delete all demo team
print("\n[12/13] Cleaning Team Members...")
count = TeamMember.objects.count()
if count > 0:
    TeamMember.objects.all().delete()
    deleted_count['TeamMember'] = count
    print(f"   ✓ Deleted {count} demo team members")
else:
    print(f"   ✓ No team members to delete")

# 13. CERTIFICATES - Delete all demo certificates
print("\n[13/13] Cleaning Certificates...")
count = Certificate.objects.count()
if count > 0:
    Certificate.objects.all().delete()
    deleted_count['Certificate'] = count
    print(f"   ✓ Deleted {count} demo certificates")
else:
    print(f"   ✓ No certificates to delete")

# Summary
print("\n" + "=" * 80)
print("  ✓ CLEANUP COMPLETED!")
print("=" * 80)
print("\nDeleted Items:")
total = 0
for model, count in deleted_count.items():
    print(f"  • {model}: {count}")
    total += count
print(f"\nTotal deleted: {total} items")

print("\nRemaining Real Client Data:")
print(f"  • Hero Slides: {HeroSlide.objects.count()}")
print(f"  • Company Features: {CompanyFeature.objects.count()}")
print(f"  • Statistics: {Statistic.objects.count()}")
print(f"  • Product Categories: {ProductCategory.objects.count()}")
print(f"  • Process Steps: {ProcessStep.objects.count()}")
print(f"  • FAQs: {FAQ.objects.count()}")
print(f"  • News: {News.objects.count()}")

print("\n" + "=" * 80)
print("Database is now clean with only real client data!")
print("=" * 80)
