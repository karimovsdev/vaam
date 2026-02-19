"""
Download real images from Unsplash and update database records.
Run on server: cd /home/vaam/app && sudo -u vaam venv/bin/python seed_images.py
"""
import os
import sys
import django
import urllib.request
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from django.conf import settings
from core.models import (
    HeroSlide, Product, Project, News, Brand, Service,
    CompanyInfo, SiteSettings
)

MEDIA_ROOT = settings.MEDIA_ROOT

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def download_image(url, filepath, retries=3):
    """Download image from URL to filepath."""
    full_path = os.path.join(MEDIA_ROOT, filepath)
    ensure_dir(full_path)
    if os.path.exists(full_path):
        print(f"  [exists] {filepath}")
        return True
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, timeout=30) as response:
                with open(full_path, 'wb') as f:
                    f.write(response.read())
            print(f"  [OK] {filepath}")
            return True
        except Exception as e:
            print(f"  [retry {attempt+1}] {filepath}: {e}")
            time.sleep(2)
    print(f"  [FAIL] {filepath}")
    return False

print("=" * 50)
print("  Downloading images for VAAM...")
print("=" * 50)

# Unsplash source URLs (free, no API key needed)
# Using specific photo IDs for consistent, relevant images

# ============ HERO SLIDES ============
print("\n[1/7] Hero Slides...")
hero_images = [
    ("https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1920&h=1080&fit=crop", "hero/hero-slide-1.jpg"),
    ("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=1920&h=1080&fit=crop", "hero/hero-slide-2.jpg"),
    ("https://images.unsplash.com/photo-1559302504-64aae6ca6b6d?w=1920&h=1080&fit=crop", "hero/hero-slide-3.jpg"),
]
for slide, (url, path) in zip(HeroSlide.objects.all().order_by('order'), hero_images):
    if download_image(url, path):
        slide.image = path
        slide.save()

# ============ PRODUCTS ============
print("\n[2/7] Products...")
product_images = {
    "longi-hi-mo-6-explorer-580w": ("https://images.unsplash.com/photo-1611365892117-00ac6fb25bab?w=800&h=600&fit=crop", "products/longi-hi-mo-6.jpg"),
    "ja-solar-deepblue-4-pro-555w": ("https://images.unsplash.com/photo-1558449028-b53a39d100fc?w=800&h=600&fit=crop", "products/ja-solar-deepblue.jpg"),
    "trina-solar-vertex-s-plus-445w": ("https://images.unsplash.com/photo-1595437193398-f24279553f4f?w=800&h=600&fit=crop", "products/trina-vertex.jpg"),
    "canadian-solar-hiku7-600w": ("https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800&h=600&fit=crop", "products/canadian-solar-hiku.jpg"),
    "huawei-sun2000-10ktl-m1": ("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&h=600&fit=crop", "products/huawei-inverter.jpg"),
    "sma-sunny-tripower-15000tl": ("https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&h=600&fit=crop", "products/sma-inverter.jpg"),
    "growatt-min-6000tl-xh": ("https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?w=800&h=600&fit=crop", "products/growatt-inverter.jpg"),
    "clenergy-pv-ezrack-solarroof-pro": ("https://images.unsplash.com/photo-1545208942-e1c9c916524b?w=800&h=600&fit=crop", "products/mounting-system.jpg"),
    "k2-systems-d-dome-ground-mount": ("https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=800&h=600&fit=crop", "products/ground-mount.jpg"),
    "huawei-luna2000-15-s0": ("https://images.unsplash.com/photo-1593941707882-a5bba14938c7?w=800&h=600&fit=crop", "products/battery-storage.jpg"),
    "solar-dc-cable-6mm-100m": ("https://images.unsplash.com/photo-1558346490-a72e53ae2d4f?w=800&h=600&fit=crop", "products/solar-cables.jpg"),
    "huawei-smart-dongle-wlan": ("https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&h=600&fit=crop", "products/smart-dongle.jpg"),
}
for product in Product.objects.all():
    if product.slug in product_images:
        url, path = product_images[product.slug]
        if download_image(url, path):
            product.image = path
            product.save()

# ============ SERVICES ============
print("\n[3/7] Services...")
service_images = {
    "solar-system-consultation": ("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&h=600&fit=crop", "services/consultation.jpg"),
    "engineering-project-management": ("https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=800&h=600&fit=crop", "services/engineering.jpg"),
    "solar-panel-supply": ("https://images.unsplash.com/photo-1558449028-b53a39d100fc?w=800&h=600&fit=crop", "services/panel-supply.jpg"),
    "inverter-equipment-supply": ("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&h=600&fit=crop", "services/equipment-supply.jpg"),
    "residential-solar-installation": ("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=800&h=600&fit=crop", "services/residential-install.jpg"),
    "commercial-industrial-installation": ("https://images.unsplash.com/photo-1497440001374-f26997328c1b?w=800&h=600&fit=crop", "services/commercial-install.jpg"),
    "preventive-maintenance": ("https://images.unsplash.com/photo-1621905252507-b35492cc74b4?w=800&h=600&fit=crop", "services/maintenance.jpg"),
    "repair-troubleshooting": ("https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800&h=600&fit=crop", "services/repair.jpg"),
}
for service in Service.objects.all():
    if service.slug in service_images:
        url, path = service_images[service.slug]
        if download_image(url, path):
            service.image = path
            service.save()

# ============ PROJECTS ============
print("\n[4/7] Projects...")
project_images = {
    "villa-solar-mardakan": ("https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=800&h=600&fit=crop", "projects/villa-mardakan.jpg"),
    "apartment-complex-yasamal": ("https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&h=600&fit=crop", "projects/apartment-yasamal.jpg"),
    "office-tower-port-baku": ("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&h=600&fit=crop", "projects/office-port-baku.jpg"),
    "ganjlik-mall-rooftop": ("https://images.unsplash.com/photo-1567449303078-57ad995bd329?w=800&h=600&fit=crop", "projects/ganjlik-mall.jpg"),
    "factory-solar-sumgait": ("https://images.unsplash.com/photo-1611365892117-00ac6fb25bab?w=800&h=600&fit=crop", "projects/factory-sumgait.jpg"),
    "warehouse-solar-kesla": ("https://images.unsplash.com/photo-1545208942-e1c9c916524b?w=800&h=600&fit=crop", "projects/warehouse-kesla.jpg"),
    "absheron-solar-farm": ("https://images.unsplash.com/photo-1509391366360-2e959784a276?w=800&h=600&fit=crop", "projects/solar-farm-absheron.jpg"),
    "gobustan-pilot-solar": ("https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=800&h=600&fit=crop", "projects/gobustan-solar.jpg"),
}
for project in Project.objects.all():
    if project.slug in project_images:
        url, path = project_images[project.slug]
        if download_image(url, path):
            project.image = path
            project.save()

# ============ NEWS ============
print("\n[5/7] News...")
news_images = {
    "azerbaijan-sets-2030-target-2gw-solar": ("https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&h=500&fit=crop", "news/azerbaijan-2030-solar.jpg"),
    "vaam-opens-new-distribution-center": ("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&h=500&fit=crop", "news/distribution-center.jpg"),
    "understanding-n-type-topcon-solar-cells": ("https://images.unsplash.com/photo-1595437193398-f24279553f4f?w=800&h=500&fit=crop", "news/topcon-technology.jpg"),
    "solar-panel-prices-record-low-2025": ("https://images.unsplash.com/photo-1559302504-64aae6ca6b6d?w=800&h=500&fit=crop", "news/solar-prices.jpg"),
    "vaam-achieves-iso-9001-certification": ("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&h=500&fit=crop", "news/iso-certification.jpg"),
    "cop30-solar-adoption-developing-markets": ("https://images.unsplash.com/photo-1497440001374-f26997328c1b?w=800&h=500&fit=crop", "news/cop30-solar.jpg"),
}
for article in News.objects.all():
    if article.slug in news_images:
        url, path = news_images[article.slug]
        if download_image(url, path):
            article.image = path
            article.save()

# ============ BRANDS ============
print("\n[6/7] Brand Logos...")
# Generate simple colored placeholder logos for brands since we can't get real logos
brand_colors = {
    "Longi Green Energy": "#E31937",
    "JA Solar": "#0066B3",
    "Trina Solar": "#003DA5",
    "Canadian Solar": "#CE1126",
    "Huawei FusionSolar": "#CF0A2C",
    "SMA Solar Technology": "#0078D6",
    "Growatt": "#00A651",
    "K2 Systems": "#1B1B1B",
    "Clenergy": "#0098DB",
    "Jinko Solar": "#003366",
}

# Create SVG logos for brands
for brand in Brand.objects.all().order_by('order'):
    brand_name = brand.name
    color = brand_colors.get(brand_name, "#333333")
    short_name = brand_name.split()[0]  # First word
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="120" viewBox="0 0 300 120">
  <rect width="300" height="120" fill="white" rx="8"/>
  <rect x="2" y="2" width="296" height="116" fill="white" rx="6" stroke="{color}" stroke-width="2"/>
  <text x="150" y="65" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="bold" fill="{color}" text-anchor="middle" dominant-baseline="middle">{short_name}</text>
  <text x="150" y="95" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#888" text-anchor="middle">SOLAR</text>
</svg>'''
    filepath = f"brands/{short_name.lower()}-logo.svg"
    full_path = os.path.join(MEDIA_ROOT, filepath)
    ensure_dir(full_path)
    with open(full_path, 'w') as f:
        f.write(svg_content)
    brand.logo = filepath
    brand.save()
    print(f"  [OK] {filepath}")

# ============ COMPANY / ABOUT ============
print("\n[7/7] About Page Image...")
about_url = "https://images.unsplash.com/photo-1497440001374-f26997328c1b?w=800&h=600&fit=crop"
about_path = "about/company-about.jpg"
if download_image(about_url, about_path):
    info = CompanyInfo.objects.get(pk=1)
    info.image = about_path
    info.save()

print()
print("=" * 50)
print("  ✓ All images downloaded and updated!")
print("=" * 50)

# Summary
total_files = 0
for root, dirs, files in os.walk(MEDIA_ROOT):
    total_files += len(files)
print(f"\n  Total media files: {total_files}")
