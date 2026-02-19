"""
Seed script for VAAM Import and Export Trading website.
Populates the database with realistic English draft data for a solar energy trading company.
Run on server: cd /home/vaam/app && sudo -u vaam venv/bin/python manage.py shell < seed_data.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from core.models import (
    SiteSettings, HeroSlide, CompanyInfo, CompanyFeature, Statistic,
    Menu, MenuItem, Page,
    ProductCategory, Product, ProductSpecification,
    ServiceCategory, Service,
    ProcessStep,
    ProjectCategory, Project,
    NewsCategory, News,
    FAQ, Testimonial, Brand
)

print("=" * 50)
print("  Seeding VAAM Database...")
print("=" * 50)

# ============ SITE SETTINGS ============
print("[1/14] Site Settings...")
settings, _ = SiteSettings.objects.get_or_create(pk=1)
settings.site_name_en = "VAAM Import and Export Trading"
settings.site_description_en = "Leading solar energy solutions provider specializing in high-quality solar panels, inverters, and complete photovoltaic systems for residential, commercial, and industrial applications."
settings.phone = "+994 50 123 45 67"
settings.phone2 = "+994 12 456 78 90"
settings.email = "info@vaamtrading.com"
settings.email2 = "sales@vaamtrading.com"
settings.address_en = "28 May Street, Baku, Azerbaijan AZ1000"
settings.address2_en = "Warehouse: Keşlə Industrial Zone, Baku"
settings.whatsapp = "994501234567"
settings.working_hours_en = "Mon - Fri: 09:00 - 18:00 | Sat: 10:00 - 15:00"
settings.facebook = "https://facebook.com/vaamtrading"
settings.linkedin = "https://linkedin.com/company/vaamtrading"
settings.instagram = "https://instagram.com/vaamtrading"
settings.youtube = "https://youtube.com/@vaamtrading"
settings.meta_title_en = "VAAM Trading | Premium Solar Energy Solutions in Azerbaijan"
settings.meta_description_en = "VAAM Import and Export Trading - Your trusted partner for solar panels, inverters, and renewable energy systems. Quality products, expert installation, and reliable service."
settings.meta_keywords_en = "solar panels, solar energy, renewable energy, photovoltaic, inverters, Azerbaijan, Baku, solar installation"
settings.google_maps_embed = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3039.2!2d49.8671!3d40.4093!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDDCsDI0JzM0LjAiTiA0OcKwNTInMDEuNiJF!5e0!3m2!1sen!2saz!4v1"
settings.save()

# ============ HERO SLIDES ============
print("[2/14] Hero Slides...")
HeroSlide.objects.all().delete()
slides = [
    {
        "title_en": "Engineering the Future of Solar Energy",
        "subtitle_en": "Powering Tomorrow, Today",
        "description_en": "Premium solar panels for global markets. We deliver cutting-edge photovoltaic solutions that maximize energy output and minimize environmental impact.",
        "button1_text_en": "Get a Quote",
        "button1_url": "/en/contact/",
        "button2_text_en": "Our Products",
        "button2_url": "/en/products/",
        "order": 1,
    },
    {
        "title_en": "Trusted by Industry Leaders Worldwide",
        "subtitle_en": "10+ Years of Excellence",
        "description_en": "From residential rooftops to large-scale solar farms, VAAM Trading delivers reliable, high-efficiency solar solutions backed by international certifications.",
        "button1_text_en": "View Projects",
        "button1_url": "/en/projects/",
        "button2_text_en": "Learn More",
        "button2_url": "/en/about/",
        "order": 2,
    },
    {
        "title_en": "Complete Solar Solutions Under One Roof",
        "subtitle_en": "Import • Supply • Install",
        "description_en": "End-to-end solar energy solutions including consultation, system design, equipment supply, installation, and after-sales maintenance.",
        "button1_text_en": "Our Services",
        "button1_url": "/en/services/",
        "button2_text_en": "Contact Us",
        "button2_url": "/en/contact/",
        "order": 3,
    },
]
for s in slides:
    HeroSlide.objects.create(**s, image="hero/placeholder.jpg")

# ============ COMPANY INFO ============
print("[3/14] Company Info...")
info, _ = CompanyInfo.objects.get_or_create(pk=1)
info.title_en = "About VAAM Trading"
info.subtitle_en = "Your Trusted Solar Energy Partner Since 2014"
info.description_en = """VAAM Import and Export Trading is a leading provider of solar energy solutions based in Baku, Azerbaijan. Since our establishment in 2014, we have been at the forefront of the renewable energy revolution in the Caucasus region and beyond.

We specialize in importing and distributing premium solar panels, inverters, mounting systems, and complete photovoltaic solutions from world-renowned manufacturers. Our partnerships with top-tier brands ensure that our clients receive only the highest quality equipment backed by international warranties and certifications.

With a dedicated team of engineers and energy consultants, we provide comprehensive support from initial consultation and system design to installation supervision and after-sales service. Our commitment to quality, reliability, and customer satisfaction has made us the preferred choice for residential, commercial, and industrial solar projects."""
info.mission_en = "To accelerate the adoption of clean solar energy across Azerbaijan and the broader region by providing world-class photovoltaic products, expert engineering support, and exceptional customer service that delivers measurable value to every client."
info.vision_en = "To become the leading solar energy solutions provider in the Caucasus and Central Asian markets, powering a sustainable future through innovation, quality, and unwavering commitment to renewable energy excellence."
info.values_en = """Quality First: We source only premium products from certified manufacturers with proven track records.
Customer Focus: Every project is tailored to meet the unique energy needs and goals of our clients.
Innovation: We continuously explore and adopt the latest solar technologies and best practices.
Sustainability: We are committed to reducing carbon footprints and promoting clean energy adoption.
Integrity: Transparent pricing, honest consultation, and reliable partnerships define our business."""
info.history_en = """2014 - Founded in Baku as a solar equipment import company
2016 - Established partnerships with leading Chinese and European solar manufacturers
2017 - Completed first large-scale commercial solar installation (500kW)
2019 - Expanded operations to Georgia and Turkey
2020 - Launched residential solar solutions division
2022 - Reached 50MW cumulative installed capacity milestone
2023 - Opened new 2,000m² warehouse and distribution center in Baku
2024 - Expanded product line to include energy storage systems
2025 - Achieved ISO 9001:2015 certification"""
info.save()

# ============ COMPANY FEATURES ============
print("[4/14] Company Features & Statistics...")
CompanyFeature.objects.all().delete()
features = [
    ("Premium Quality Products", "We exclusively source Tier-1 solar panels and equipment from globally certified manufacturers ensuring maximum efficiency and longevity.", "fas fa-award", 1),
    ("Expert Engineering Team", "Our team of certified solar engineers provides professional system design, installation supervision, and technical support.", "fas fa-hard-hat", 2),
    ("10+ Years Experience", "With over a decade in the solar industry, we bring unmatched expertise and reliability to every project we undertake.", "fas fa-calendar-check", 3),
    ("Complete Solutions", "From initial consultation to installation and maintenance, we offer end-to-end solar energy solutions under one roof.", "fas fa-solar-panel", 4),
    ("International Warranty", "All our products come with comprehensive international warranties, giving you peace of mind and long-term protection.", "fas fa-shield-alt", 5),
    ("Competitive Pricing", "Direct partnerships with manufacturers allow us to offer premium products at the most competitive prices in the region.", "fas fa-tags", 6),
]
for title, desc, icon, order in features:
    CompanyFeature.objects.create(title_en=title, description_en=desc, icon=icon, order=order)

# ============ STATISTICS ============
Statistic.objects.all().delete()
stats = [
    ("Completed Projects", 350, "+", "fas fa-project-diagram", 1),
    ("MW Installed", 50, "+", "fas fa-bolt", 2),
    ("Happy Clients", 500, "+", "fas fa-users", 3),
    ("Years Experience", 10, "+", "fas fa-calendar-alt", 4),
]
for title, value, suffix, icon, order in stats:
    Statistic.objects.create(title_en=title, value=value, suffix=suffix, icon=icon, order=order)

# ============ PRODUCT CATEGORIES & PRODUCTS ============
print("[5/14] Product Categories & Products...")
ProductCategory.objects.all().delete()
categories_data = [
    ("Solar Panels", "solar-panels", "High-efficiency monocrystalline, polycrystalline, and bifacial solar panels from leading manufacturers. Designed for residential, commercial, and utility-scale applications.", "fas fa-solar-panel", 1),
    ("Solar Inverters", "solar-inverters", "Premium string inverters, microinverters, and hybrid inverters for optimal energy conversion and system monitoring.", "fas fa-exchange-alt", 2),
    ("Mounting Systems", "mounting-systems", "Durable aluminum and steel mounting structures for rooftop, ground-mount, and carport solar installations.", "fas fa-tools", 3),
    ("Energy Storage", "energy-storage", "Advanced lithium-ion battery storage systems for residential and commercial energy independence.", "fas fa-battery-full", 4),
    ("Solar Cables & Connectors", "solar-cables-connectors", "UV-resistant solar cables, MC4 connectors, and wiring accessories for safe and efficient system connections.", "fas fa-plug", 5),
    ("Monitoring Systems", "monitoring-systems", "Smart monitoring solutions for real-time tracking of solar system performance and energy production.", "fas fa-chart-line", 6),
]
cat_objects = {}
for name, slug, desc, icon, order in categories_data:
    cat = ProductCategory.objects.create(name_en=name, slug=slug, description_en=desc, icon=icon, order=order)
    cat_objects[slug] = cat

# Products
products_data = [
    # Solar Panels
    ("solar-panels", "Longi Hi-MO 6 Explorer 580W", "longi-hi-mo-6-explorer-580w",
     "Latest generation monocrystalline PERC solar panel with 22.5% efficiency. Ideal for residential and commercial rooftop installations.",
     """<p>The Longi Hi-MO 6 Explorer 580W solar panel represents the pinnacle of monocrystalline PERC technology. With an impressive 22.5% module efficiency, this panel delivers exceptional power output even in limited roof space.</p>
<p><strong>Key Features:</strong></p>
<ul>
<li>580W maximum power output</li>
<li>22.5% module efficiency</li>
<li>Half-cut cell technology for reduced hot-spot risk</li>
<li>Multi-busbar design for improved current collection</li>
<li>25-year product warranty, 30-year performance warranty</li>
<li>Excellent low-light performance</li>
</ul>""",
     "Contact for Price", True, 1,
     [("Power Output", "580W"), ("Efficiency", "22.5%"), ("Cell Type", "Monocrystalline PERC"), ("Dimensions", "2278 × 1134 × 30 mm"), ("Weight", "28.5 kg"), ("Warranty", "25 years product / 30 years performance")]),

    ("solar-panels", "JA Solar DeepBlue 4.0 Pro 555W", "ja-solar-deepblue-4-pro-555w",
     "High-performance n-type TOPCon solar panel with advanced passivation technology for superior yields.",
     """<p>The JA Solar DeepBlue 4.0 Pro leverages cutting-edge n-type TOPCon cell technology to deliver outstanding energy yields. With lower degradation rates and excellent temperature coefficients, this panel is ideal for maximizing long-term return on investment.</p>
<p><strong>Key Features:</strong></p>
<ul>
<li>555W power output with n-type TOPCon cells</li>
<li>22.4% module efficiency</li>
<li>Bifacial design with up to 25% rear-side gain</li>
<li>0.4%/year degradation rate</li>
<li>Enhanced performance in high-temperature conditions</li>
</ul>""",
     "Contact for Price", True, 2,
     [("Power Output", "555W"), ("Efficiency", "22.4%"), ("Cell Type", "N-type TOPCon"), ("Bifacial", "Yes, up to 25% gain"), ("Dimensions", "2278 × 1134 × 30 mm"), ("Warranty", "25 years product / 30 years performance")]),

    ("solar-panels", "Trina Solar Vertex S+ 445W", "trina-solar-vertex-s-plus-445w",
     "Compact high-efficiency panel perfect for residential rooftops with limited space.",
     """<p>The Trina Solar Vertex S+ 445W is designed specifically for residential applications. Its compact form factor and high efficiency make it the ideal choice for homeowners looking to maximize solar generation on limited roof space.</p>""",
     "Contact for Price", False, 3,
     [("Power Output", "445W"), ("Efficiency", "22.2%"), ("Cell Type", "N-type i-TOPCon"), ("Dimensions", "1762 × 1134 × 30 mm"), ("Weight", "21.8 kg"), ("Warranty", "25 years product / 25 years performance")]),

    ("solar-panels", "Canadian Solar HiKu7 600W", "canadian-solar-hiku7-600w",
     "Utility-scale bifacial module with industry-leading power output for large solar farms.",
     """<p>The Canadian Solar HiKu7 600W module is engineered for utility-scale solar farms and large commercial installations. With 600W power output and bifacial technology, it delivers exceptional energy density and lowest LCOE.</p>""",
     "Contact for Price", False, 4,
     [("Power Output", "600W"), ("Efficiency", "22.5%"), ("Cell Type", "N-type TOPCon"), ("Bifacial", "Yes, up to 30% gain"), ("Dimensions", "2384 × 1134 × 30 mm"), ("Warranty", "25 years / 30 years performance")]),

    # Solar Inverters
    ("solar-inverters", "Huawei SUN2000-10KTL-M1", "huawei-sun2000-10ktl-m1",
     "Smart string inverter with built-in optimizer for residential and small commercial systems.",
     """<p>The Huawei SUN2000-10KTL-M1 is a premium residential string inverter featuring AI-powered MPPT tracking, built-in PID recovery, and seamless integration with Huawei's FusionSolar monitoring platform.</p>
<p><strong>Features:</strong></p>
<ul>
<li>10kW AC output power</li>
<li>98.6% maximum efficiency</li>
<li>Built-in smart I-V curve diagnosis</li>
<li>Integrated DC disconnect switch</li>
<li>FusionSolar app monitoring</li>
</ul>""",
     "Contact for Price", True, 1,
     [("AC Power", "10 kW"), ("Max Efficiency", "98.6%"), ("MPPT Trackers", "2"), ("Communication", "WiFi / 4G / RS485"), ("Protection", "IP65"), ("Warranty", "10 years (extendable to 25)")]),

    ("solar-inverters", "SMA Sunny Tripower 15000TL", "sma-sunny-tripower-15000tl",
     "Premium German-engineered three-phase inverter for commercial rooftop installations.",
     """<p>SMA's Sunny Tripower 15000TL delivers German engineering excellence for commercial solar systems. With its wide input voltage range and advanced shade management, it ensures maximum yield under all conditions.</p>""",
     "Contact for Price", True, 2,
     [("AC Power", "15 kW"), ("Max Efficiency", "98.8%"), ("MPPT Trackers", "2"), ("Communication", "Ethernet / WiFi"), ("Protection", "IP65"), ("Warranty", "10 years (extendable to 25)")]),

    ("solar-inverters", "Growatt MIN 6000TL-XH", "growatt-min-6000tl-xh",
     "Cost-effective hybrid inverter with battery support for homes seeking energy independence.",
     """<p>The Growatt MIN 6000TL-XH is a hybrid inverter that supports both grid-tied and battery storage configurations. Perfect for homeowners looking to achieve energy independence with a cost-effective solution.</p>""",
     "Contact for Price", False, 3,
     [("AC Power", "6 kW"), ("Max Efficiency", "97.6%"), ("Battery Support", "Yes, 48V lithium"), ("MPPT Trackers", "2"), ("Communication", "WiFi / RS485"), ("Warranty", "10 years")]),

    # Mounting Systems
    ("mounting-systems", "Clenergy PV-ezRack SolarRoof Pro", "clenergy-pv-ezrack-solarroof-pro",
     "Versatile aluminum rail-based mounting system for pitched and flat roof installations.",
     """<p>The Clenergy PV-ezRack SolarRoof Pro is an industry-leading aluminum mounting system engineered for rapid installation on virtually any roof type. Pre-assembled components reduce installation time by up to 50%.</p>""",
     "Contact for Price", True, 1,
     [("Material", "Anodized Aluminum 6005-T5"), ("Wind Load", "Up to 60 m/s"), ("Snow Load", "Up to 1.5 kN/m²"), ("Roof Type", "Pitched / Flat / Metal"), ("Warranty", "15 years"), ("Certification", "AS/NZS 1170, EN 1991")]),

    ("mounting-systems", "K2 Systems D-Dome Ground Mount", "k2-systems-d-dome-ground-mount",
     "Heavy-duty steel ground mounting system for utility-scale solar farms and open-field installations.",
     """<p>K2 Systems D-Dome is a premium ground-mount solution designed for large-scale solar farms. Its innovative design allows for quick assembly and optimal panel tilt angles for maximum energy harvest.</p>""",
     "Contact for Price", False, 2,
     [("Material", "Hot-dip Galvanized Steel"), ("Foundation", "Driven pile / Screw"), ("Tilt Angle", "10° - 40° adjustable"), ("Wind Load", "Up to 55 m/s"), ("Warranty", "20 years"), ("Certification", "Eurocode EN 1991")]),

    # Energy Storage
    ("energy-storage", "Huawei LUNA2000-15-S0 Battery", "huawei-luna2000-15-s0",
     "Modular lithium iron phosphate battery system for residential energy storage and backup.",
     """<p>The Huawei LUNA2000-15-S0 is a modular battery storage system that integrates seamlessly with Huawei SUN2000 inverters. Its LFP chemistry ensures maximum safety and a 15-year service life.</p>""",
     "Contact for Price", True, 1,
     [("Capacity", "15 kWh (scalable to 30 kWh)"), ("Chemistry", "Lithium Iron Phosphate (LFP)"), ("Voltage", "600V DC"), ("Depth of Discharge", "100%"), ("Cycles", "6,000+"), ("Warranty", "10 years")]),

    # Cables & Connectors
    ("solar-cables-connectors", "Solar DC Cable 6mm² (100m)", "solar-dc-cable-6mm-100m",
     "UV-resistant, double-insulated 6mm² PV cable rated for 1500V DC solar installations.",
     """<p>Premium quality solar DC cable specifically designed for photovoltaic installations. Double TUV-certified with excellent UV resistance and a 25+ year service life.</p>""",
     "Contact for Price", False, 1,
     [("Cross Section", "6 mm²"), ("Voltage Rating", "1500V DC"), ("Temperature Range", "-40°C to +90°C"), ("Insulation", "Double (XLPE/LSZH)"), ("UV Resistance", "EN 50618"), ("Length", "100m roll")]),

    # Monitoring
    ("monitoring-systems", "Huawei Smart Dongle-WLAN-FE", "huawei-smart-dongle-wlan",
     "WiFi-enabled smart monitoring dongle for real-time solar system performance tracking via FusionSolar app.",
     """<p>The Huawei Smart Dongle enables wireless monitoring of your solar system through the FusionSolar cloud platform. Track energy production, system health, and savings from your smartphone anytime, anywhere.</p>""",
     "Contact for Price", False, 1,
     [("Connectivity", "WiFi 802.11 b/g/n"), ("Compatible Inverters", "Huawei SUN2000 series"), ("Monitoring", "Real-time via FusionSolar app"), ("Data Storage", "Cloud-based, 25 years"), ("Installation", "Plug & Play USB"), ("Warranty", "5 years")]),
]

for cat_slug, name, slug, short_desc, desc, price, featured, order, specs in products_data:
    p = Product.objects.create(
        category=cat_objects[cat_slug],
        name_en=name, slug=slug,
        short_description_en=short_desc,
        description_en=desc,
        image="products/placeholder.jpg",
        price=price, is_featured=featured, order=order
    )
    for i, (key, value) in enumerate(specs):
        ProductSpecification.objects.create(product=p, key_en=key, value_en=value, order=i)

# ============ SERVICE CATEGORIES & SERVICES ============
print("[6/14] Services...")
ServiceCategory.objects.all().delete()
svc_cats = [
    ("Consultation & Design", "consultation-design", 1),
    ("Supply & Distribution", "supply-distribution", 2),
    ("Installation", "installation", 3),
    ("Maintenance & Support", "maintenance-support", 4),
]
svc_cat_objects = {}
for name, slug, order in svc_cats:
    sc = ServiceCategory.objects.create(name_en=name, slug=slug, order=order)
    svc_cat_objects[slug] = sc

services_data = [
    ("consultation-design", "Solar System Consultation", "solar-system-consultation",
     "Expert energy assessment and custom solar system design tailored to your specific needs and budget.",
     """<p>Our experienced solar engineers conduct thorough site assessments and energy audits to design the optimal solar system for your property. We analyze your energy consumption patterns, roof conditions, shading factors, and local regulations to create a custom solution that maximizes your return on investment.</p>
<p>Every consultation includes detailed 3D modeling, energy yield simulations, and comprehensive financial analysis showing projected savings and payback periods.</p>""",
     "fas fa-drafting-compass",
     "Free on-site energy assessment\nDetailed 3D system design and modeling\nEnergy yield simulation and analysis\nROI and payback period calculation\nPermit documentation support\nGrid connection consultation",
     1),

    ("consultation-design", "Engineering & Project Management", "engineering-project-management",
     "Professional engineering oversight and project management for solar installations of all scales.",
     """<p>Our engineering team provides professional project management services from concept to commissioning. We ensure every installation meets the highest technical standards and complies with all local and international regulations.</p>""",
     "fas fa-cogs",
     "Detailed engineering drawings\nStructural analysis and calculations\nElectrical system design\nProject timeline management\nQuality assurance inspections\nCommissioning and handover",
     2),

    ("supply-distribution", "Solar Panel Supply", "solar-panel-supply",
     "Direct import and distribution of premium solar panels from world-leading manufacturers.",
     """<p>As an authorized distributor for multiple Tier-1 solar panel manufacturers, VAAM Trading offers competitive pricing on the latest high-efficiency solar modules. Our direct relationships with factories ensure authentic products with full manufacturer warranties.</p>""",
     "fas fa-solar-panel",
     "Tier-1 branded solar panels\nFull manufacturer warranty\nBulk pricing for large orders\nFast delivery from local warehouse\nCustom order arrangements\nTechnical documentation included",
     3),

    ("supply-distribution", "Inverter & Equipment Supply", "inverter-equipment-supply",
     "Complete range of inverters, batteries, mounting systems, and Balance of System components.",
     """<p>We stock a comprehensive range of solar equipment including string inverters, hybrid inverters, lithium battery storage systems, mounting structures, cables, and all necessary BOS components for any type of solar installation.</p>""",
     "fas fa-warehouse",
     "String, hybrid, and micro inverters\nLithium battery storage systems\nMounting structures for all roof types\nSolar cables and MC4 connectors\nProtection and monitoring equipment\nAll products carry manufacturer warranty",
     4),

    ("installation", "Residential Solar Installation", "residential-solar-installation",
     "Professional rooftop solar installation for homes with comprehensive warranty and support.",
     """<p>Transform your home into a clean energy powerhouse with our residential solar installation service. Our certified installers handle everything from panel mounting to electrical connections, ensuring a safe, efficient, and aesthetically pleasing installation.</p>""",
     "fas fa-home",
     "Professional site survey\nOptimal panel placement design\nCertified installation team\nGrid connection and net metering setup\nSystem testing and commissioning\n5-year workmanship warranty",
     5),

    ("installation", "Commercial & Industrial Installation", "commercial-industrial-installation",
     "Large-scale solar installations for businesses, factories, and industrial facilities.",
     """<p>Reduce your business electricity costs by up to 80% with our commercial and industrial solar solutions. We design and install systems ranging from 50kW to multi-MW scale, optimized for your facility's energy profile and operational requirements.</p>""",
     "fas fa-industry",
     "Custom system design for commercial loads\nRooftop and ground-mount options\nHigh-voltage system expertise\nSCADA monitoring integration\nPower purchase agreement (PPA) support\n10-year workmanship warranty",
     6),

    ("maintenance-support", "Preventive Maintenance", "preventive-maintenance",
     "Regular inspection and maintenance programs to keep your solar system performing at peak efficiency.",
     """<p>Protect your solar investment with our comprehensive preventive maintenance packages. Regular cleaning, inspection, and performance monitoring ensure your system operates at maximum efficiency throughout its 25+ year lifespan.</p>""",
     "fas fa-wrench",
     "Quarterly panel cleaning\nAnnual thermal imaging inspection\nInverter health checks\nConnection tightness verification\nPerformance monitoring and reporting\nPriority emergency support",
     7),

    ("maintenance-support", "Repair & Troubleshooting", "repair-troubleshooting",
     "Fast diagnosis and repair services for underperforming or damaged solar systems.",
     """<p>If your solar system isn't performing as expected, our technical team can quickly diagnose and resolve any issues. We service all brands and system types with genuine replacement parts and expert technicians.</p>""",
     "fas fa-tools",
     "Remote system diagnosis\nOn-site troubleshooting\nPanel replacement and repair\nInverter service and replacement\nWiring and connector repair\nWarranty claim processing",
     8),
]

for cat_slug, title, slug, short, desc, icon, feats, order in services_data:
    Service.objects.create(
        category=svc_cat_objects[cat_slug],
        title_en=title, slug=slug,
        short_description_en=short,
        description_en=desc,
        icon=icon, features_en=feats, order=order
    )

# ============ PROCESS STEPS ============
print("[7/14] Process Steps...")
ProcessStep.objects.all().delete()
steps = [
    ("Consultation", "We start with a thorough assessment of your energy needs, site conditions, and budget to determine the best solar solution for you.", "fas fa-comments", 1),
    ("System Design", "Our engineers create a custom system design with detailed 3D modeling, energy yield projections, and financial analysis.", "fas fa-pencil-ruler", 2),
    ("Proposal & Agreement", "You receive a comprehensive proposal with transparent pricing, timeline, and warranty details for your approval.", "fas fa-file-signature", 3),
    ("Equipment Supply", "We source and deliver premium solar equipment directly from our warehouse, ensuring quality and timely availability.", "fas fa-truck", 4),
    ("Installation", "Our certified installers mount and connect your system following strict safety and quality standards.", "fas fa-hard-hat", 5),
    ("Commissioning", "After thorough testing, your system is connected to the grid and you start generating clean solar energy.", "fas fa-check-circle", 6),
]
for title, desc, icon, order in steps:
    ProcessStep.objects.create(title_en=title, description_en=desc, icon=icon, order=order)

# ============ PROJECT CATEGORIES & PROJECTS ============
print("[8/14] Projects...")
ProjectCategory.objects.all().delete()
proj_cats = [
    ("Residential", "residential", 1),
    ("Commercial", "commercial", 2),
    ("Industrial", "industrial", 3),
    ("Solar Farm", "solar-farm", 4),
]
proj_cat_objects = {}
for name, slug, order in proj_cats:
    pc = ProjectCategory.objects.create(name_en=name, slug=slug, order=order)
    proj_cat_objects[slug] = pc

now = timezone.now()
projects_data = [
    ("residential", "Villa Solar Installation - Mardakan", "villa-solar-mardakan",
     "10kW rooftop solar system for a luxury villa in Mardakan, Baku.",
     """<p>Complete residential solar installation for a 350m² luxury villa in the Mardakan district. The system features 18 Longi Hi-MO 6 panels with a Huawei SUN2000-10KTL inverter, generating approximately 14,000 kWh annually and covering 95% of the household's electricity consumption.</p>""",
     "Private Client", "Mardakan, Baku", True, 1),

    ("residential", "Apartment Complex - Yasamal", "apartment-complex-yasamal",
     "25kW shared solar system for a 12-unit residential building.",
     """<p>Innovative shared solar installation on a 12-unit apartment building in Yasamal district. The net-metered system distributes solar energy to all residents, reducing collective electricity costs by 60%.</p>""",
     "Yasamal Residences LLC", "Yasamal, Baku", False, 2),

    ("commercial", "Office Tower Solar Retrofit - Port Baku", "office-tower-port-baku",
     "150kW commercial rooftop solar system for a Class A office building.",
     """<p>Large-scale commercial rooftop installation on a 15-story office tower in the Port Baku complex. The 150kW system uses 270 JA Solar DeepBlue modules with SMA Tripower inverters, reducing the building's energy costs by approximately 40%.</p>""",
     "Pasha Holding", "Port Baku, Baku", True, 3),

    ("commercial", "Shopping Mall Rooftop - Ganjlik Mall", "ganjlik-mall-rooftop",
     "200kW rooftop solar system for one of Baku's largest shopping centers.",
     """<p>A 200kW solar rooftop system installed on the expansive roof of Ganjlik Mall. The system offsets a significant portion of the mall's daytime electricity usage, particularly during peak air conditioning hours.</p>""",
     "Ganjlik Mall Management", "Ganjlik, Baku", True, 4),

    ("industrial", "Factory Solar Installation - Sumgait", "factory-solar-sumgait",
     "500kW industrial solar system for a manufacturing facility in Sumgait.",
     """<p>One of the largest industrial solar installations in Azerbaijan. This 500kW system powers a manufacturing facility in the Sumgait Industrial Zone, featuring 900 Canadian Solar HiKu7 panels with Huawei SUN2000-100KTL string inverters and advanced SCADA monitoring.</p>""",
     "Azerbaijan Industrial Corporation", "Sumgait Free Economic Zone", True, 5),

    ("industrial", "Warehouse Solar - Keşlə", "warehouse-solar-kesla",
     "120kW solar system on a logistics warehouse roof.",
     """<p>Rooftop solar installation on a 5,000m² logistics warehouse. The system provides clean energy for warehouse operations including lighting, ventilation, and electric forklift charging stations.</p>""",
     "TransCaspian Logistics", "Keşlə, Baku", False, 6),

    ("solar-farm", "Absheron Solar Farm", "absheron-solar-farm",
     "2MW ground-mount solar farm in the Absheron Peninsula.",
     """<p>VAAM Trading's flagship project: a 2MW utility-scale solar farm on 4 hectares of land in the Absheron Peninsula. The installation uses single-axis tracking technology with bifacial modules to maximize energy production throughout the day. The farm generates enough electricity to power approximately 800 homes.</p>""",
     "AzerEnergy JSC", "Absheron Peninsula", True, 7),

    ("solar-farm", "Gobustan Pilot Solar Plant", "gobustan-pilot-solar",
     "500kW pilot solar plant as part of Azerbaijan's renewable energy initiative.",
     """<p>A pilot solar power plant developed in partnership with the State Energy Agency as part of Azerbaijan's commitment to increasing renewable energy capacity. The 500kW facility serves as a demonstration project for future large-scale solar development.</p>""",
     "State Agency on Alternative and Renewable Energy", "Gobustan", False, 8),
]

for cat_slug, title, slug, short, desc, client, location, featured, order in projects_data:
    Project.objects.create(
        category=proj_cat_objects[cat_slug],
        title_en=title, slug=slug,
        short_description_en=short, description_en=desc,
        image="projects/placeholder.jpg",
        client=client, location=location,
        date_completed=(now - timedelta(days=order*60)).date(),
        is_featured=featured, order=order
    )

# ============ NEWS CATEGORIES & NEWS ============
print("[9/14] News...")
NewsCategory.objects.all().delete()
news_cats = [
    ("Industry News", "industry-news", 1),
    ("Company Updates", "company-updates", 2),
    ("Technology", "technology", 3),
    ("Market Insights", "market-insights", 4),
]
news_cat_objects = {}
for name, slug, order in news_cats:
    nc = NewsCategory.objects.create(name_en=name, slug=slug, order=order)
    news_cat_objects[slug] = nc

news_data = [
    ("industry-news", "Azerbaijan Sets 2030 Target for 2GW Solar Capacity",
     "azerbaijan-sets-2030-target-2gw-solar",
     "The government announces ambitious plans to reach 2 gigawatts of installed solar capacity by 2030, signaling major growth for the domestic solar industry.",
     """<p>In a landmark announcement at the Baku Energy Forum, Azerbaijan's Ministry of Energy revealed its updated renewable energy roadmap, targeting 2 gigawatts of installed solar capacity by 2030. This represents a 400% increase from the current installed base and positions Azerbaijan as the solar energy leader in the Caucasus region.</p>
<p>The plan includes incentives for both domestic and foreign investors, streamlined permitting processes, and a new feed-in tariff scheme designed to accelerate private sector participation in solar energy development.</p>
<p>VAAM Trading welcomes this development and stands ready to support the nation's solar energy ambitions with our extensive range of products and services.</p>""",
     True, 7, 1),

    ("company-updates", "VAAM Trading Opens New 2,000m² Distribution Center",
     "vaam-opens-new-distribution-center",
     "Our new state-of-the-art warehouse in Baku enables faster delivery and expanded inventory of solar equipment.",
     """<p>We are proud to announce the opening of our new 2,000 square meter distribution center in Baku's Keşlə industrial zone. This modern facility significantly expands our warehousing capacity and enables us to maintain larger inventories of popular solar panels, inverters, and mounting systems.</p>
<p>The new center features climate-controlled storage, efficient logistics systems, and a dedicated quality inspection area to ensure every product meets our exacting standards before reaching your project site.</p>
<p>With this expansion, most standard orders can now be fulfilled within 24-48 hours, dramatically reducing project lead times for our customers.</p>""",
     True, 5, 2),

    ("technology", "Understanding N-Type TOPCon: The Future of Solar Cells",
     "understanding-n-type-topcon-solar-cells",
     "A deep dive into next-generation n-type TOPCon solar cell technology and why it's transforming the industry.",
     """<p>N-type TOPCon (Tunnel Oxide Passivated Contact) solar cells represent the next evolutionary step in photovoltaic technology. As the solar industry moves beyond traditional PERC cells, TOPCon technology offers significant advantages in efficiency, degradation, and temperature performance.</p>
<h3>What Makes TOPCon Different?</h3>
<p>TOPCon cells use an ultra-thin tunnel oxide layer combined with a heavily doped polysilicon layer to achieve passivated contacts. This virtually eliminates carrier recombination at the cell's rear surface, boosting efficiency beyond 25%.</p>
<h3>Key Advantages</h3>
<ul>
<li>Higher efficiency: exceeding 25% cell efficiency vs 23% for PERC</li>
<li>Lower degradation: 0.4% per year vs 0.55% for PERC</li>
<li>Better temperature coefficient: -0.30%/°C vs -0.35%/°C</li>
<li>Excellent bifacial performance with up to 85% bifaciality factor</li>
</ul>
<p>At VAAM Trading, we now stock a wide range of n-type TOPCon panels from JA Solar, Longi, and Trina Solar. Contact us to learn which option is best for your project.</p>""",
     False, 8, 3),

    ("market-insights", "Solar Panel Prices Hit Record Low in 2025",
     "solar-panel-prices-record-low-2025",
     "Global solar module prices have dropped to historic lows, making solar energy more accessible than ever before.",
     """<p>Global solar module prices have reached unprecedented lows in early 2025, with utility-scale modules available below $0.10 per watt. This price decline, driven by massive manufacturing expansion in Asia, has dramatically improved the economics of solar energy worldwide.</p>
<p>For Azerbaijan, this means that the payback period for residential solar systems has shortened to just 3-5 years, while commercial installations can achieve payback in as little as 2-3 years depending on electricity consumption patterns.</p>
<p>VAAM Trading is passing these savings directly to our customers. Contact us today for updated pricing on our full range of solar products.</p>""",
     False, 4, 4),

    ("company-updates", "VAAM Trading Achieves ISO 9001:2015 Certification",
     "vaam-achieves-iso-9001-certification",
     "Our commitment to quality management is now backed by international ISO 9001:2015 certification.",
     """<p>We are pleased to announce that VAAM Import and Export Trading has been awarded ISO 9001:2015 certification for our quality management system. This internationally recognized certification covers our entire operation including procurement, warehousing, distribution, and customer service processes.</p>
<p>The certification was awarded following a rigorous audit by TÜV Rheinland and reflects our ongoing commitment to maintaining the highest standards of quality in everything we do.</p>""",
     False, 3, 5),

    ("industry-news", "COP30 Highlights: Accelerating Solar Adoption in Developing Markets",
     "cop30-solar-adoption-developing-markets",
     "Key takeaways from COP30 on how developing nations are embracing solar energy to meet climate commitments.",
     """<p>The recent COP30 climate summit in Belém, Brazil, highlighted the crucial role of solar energy in helping developing nations meet their Paris Agreement commitments. Several key announcements directly impact the solar industry in the Caucasus and Central Asian regions.</p>
<p>New international financing mechanisms were announced to support solar project development in emerging markets, and several multilateral development banks committed to increasing solar lending by 50% over the next five years.</p>""",
     False, 6, 6),
]

for cat_slug, title, slug, summary, content, featured, reading_time, order in news_data:
    News.objects.create(
        category=news_cat_objects[cat_slug],
        title_en=title, slug=slug,
        summary_en=summary, content_en=content,
        image="news/placeholder.jpg",
        author="VAAM Team",
        reading_time=reading_time,
        is_featured=featured,
        published_at=now - timedelta(days=order*12)
    )

# ============ FAQ ============
print("[10/14] FAQs...")
FAQ.objects.all().delete()
faqs = [
    ("What types of solar panels do you offer?", "We offer a wide range of Tier-1 solar panels including monocrystalline PERC, n-type TOPCon, and bifacial modules from leading manufacturers like Longi, JA Solar, Trina Solar, and Canadian Solar. Our inventory includes panels ranging from 445W to 600W for residential, commercial, and utility-scale applications.", 1),
    ("How much does a residential solar system cost?", "The cost of a residential solar system depends on several factors including system size, equipment choice, roof type, and installation complexity. A typical 5-10kW home system in Azerbaijan ranges from $4,000 to $10,000. We provide free on-site consultations with detailed cost breakdowns and ROI analysis.", 2),
    ("What is the payback period for solar panels?", "In Azerbaijan, residential solar systems typically achieve payback in 3-5 years, while commercial systems can pay back in 2-4 years. The exact payback period depends on your electricity consumption, system size, and local electricity rates. Our team provides detailed financial projections with every consultation.", 3),
    ("Do you provide installation services?", "Yes, we offer complete turnkey installation services for all types of solar systems. Our certified installation team handles everything from mounting and wiring to grid connection and commissioning. All installations come with a 5-year workmanship warranty (10 years for commercial projects).", 4),
    ("What warranties do your products carry?", "All our solar panels come with 25-year product warranties and 25-30 year performance guarantees from the manufacturer. Inverters carry 10-year warranties extendable up to 25 years. Mounting systems are warranted for 15-20 years. We handle all warranty claims on behalf of our customers.", 5),
    ("Do you offer maintenance services?", "Yes, we offer comprehensive maintenance packages including quarterly panel cleaning, annual thermal imaging inspections, inverter health checks, and 24/7 monitoring. Regular maintenance ensures your system operates at peak efficiency throughout its 25+ year lifespan.", 6),
    ("Can I use solar panels during a power outage?", "Standard grid-tied systems shut down during power outages for safety. However, if you install a hybrid inverter with battery storage, you can have backup power during outages. We offer complete hybrid solutions with Huawei LUNA2000 batteries for seamless backup power.", 7),
    ("Do you ship equipment outside of Baku?", "Yes, we deliver solar equipment throughout Azerbaijan and neighboring countries including Georgia and Turkey. Delivery times and costs vary by location. For large orders, we can arrange direct container shipping to your project site.", 8),
    ("What is net metering?", "Net metering allows you to export excess solar electricity to the grid and receive credits on your electricity bill. When your system produces more power than you consume (typically during sunny daytime hours), the surplus flows to the grid and your meter runs backwards, reducing your bill.", 9),
    ("How long does installation take?", "A typical residential installation (5-10kW) takes 1-2 days. Commercial installations (50-200kW) typically require 1-3 weeks. Large industrial and utility-scale projects are scheduled based on complexity. We provide detailed timelines with every proposal.", 10),
]
for q, a, order in faqs:
    FAQ.objects.create(question_en=q, answer_en=a, order=order)

# ============ TESTIMONIALS ============
print("[11/14] Testimonials...")
Testimonial.objects.all().delete()
testimonials = [
    ("Murad Hasanov", "Homeowner", "Private Residence, Mardakan",
     "VAAM Trading installed a 10kW solar system on my villa and the results have been outstanding. My electricity bill dropped by 90% and the installation was completed in just one day. The team was professional, knowledgeable, and always available to answer my questions. Highly recommended!", 5, 1),
    ("Leyla Aliyeva", "Facilities Manager", "Ganjlik Mall",
     "We chose VAAM for our 200kW rooftop installation based on their reputation and expertise. They delivered exactly as promised - on time, on budget, and with exceptional quality. The monitoring system they set up gives us real-time visibility into our energy savings.", 5, 2),
    ("Rashad Mammadov", "CEO", "TransCaspian Logistics",
     "The solar system VAAM installed on our warehouse has significantly reduced our operating costs. Their team handled everything from permit paperwork to grid connection. The after-sales support is equally impressive - they proactively monitor our system and address any issues before we even notice them.", 5, 3),
    ("Kamran Guliyev", "Chief Engineer", "Azerbaijan Industrial Corporation",
     "Working with VAAM on our 500kW factory installation was a seamless experience. Their engineering team designed a system perfectly suited to our power consumption profile, and the quality of equipment and installation exceeded our expectations.", 5, 4),
    ("Elena Petrova", "Director", "Green Energy Solutions Georgia",
     "As a solar installer in Georgia, we rely on VAAM Trading as our primary equipment supplier. Their range of products, competitive pricing, and reliable delivery have been instrumental to our business growth. They are a truly professional partner.", 5, 5),
    ("Tural Ahmadov", "Property Developer", "Yasamal Residences",
     "VAAM Trading helped us integrate solar energy into our new residential development. The shared solar system they designed has become a major selling point for our apartments. Their expertise in both technical and financial aspects of solar was invaluable.", 4, 6),
]
for name, position, company, content, rating, order in testimonials:
    Testimonial.objects.create(
        name=name, position=position, company=company,
        content_en=content, rating=rating, order=order
    )

# ============ BRANDS ============
print("[12/14] Brands...")
Brand.objects.all().delete()
brands = [
    ("Longi Green Energy", "https://www.longi.com", 1),
    ("JA Solar", "https://www.jasolar.com", 2),
    ("Trina Solar", "https://www.trinasolar.com", 3),
    ("Canadian Solar", "https://www.canadiansolar.com", 4),
    ("Huawei FusionSolar", "https://solar.huawei.com", 5),
    ("SMA Solar Technology", "https://www.sma.de", 6),
    ("Growatt", "https://www.growatt.com", 7),
    ("K2 Systems", "https://k2-systems.com", 8),
    ("Clenergy", "https://www.clenergy.com", 9),
    ("Jinko Solar", "https://www.jinkosolar.com", 10),
]
for name, url, order in brands:
    Brand.objects.create(name_en=name, url=url, order=order, logo="brands/placeholder.png")

# ============ MENUS ============
print("[13/14] Menus...")
Menu.objects.all().delete()
main_menu = Menu.objects.create(title="Main Navigation", slug="main-navigation", location="main")
items = [
    ("Home", "home", 1),
    ("About Us", "about", 2),
    ("Services", "services", 3),
    ("Products", "products", 4),
    ("Projects", "projects", 5),
    ("News", "news", 6),
    ("Contact", "contact", 7),
]
for title, link_type, order in items:
    MenuItem.objects.create(menu=main_menu, title_en=title, link_type=link_type, order=order)

footer_menu = Menu.objects.create(title="Footer Quick Links", slug="footer-quick-links", location="footer")
for title, link_type, order in items:
    MenuItem.objects.create(menu=footer_menu, title_en=title, link_type=link_type, order=order)

# ============ PAGES ============
print("[14/14] Pages...")
Page.objects.all().delete()
pages_data = [
    ("Privacy Policy", "privacy-policy",
     """<h2>Privacy Policy</h2>
<p>VAAM Import and Export Trading ("we," "our," or "us") respects your privacy and is committed to protecting your personal data. This privacy policy explains how we collect, use, and safeguard your information when you visit our website or use our services.</p>
<h3>Information We Collect</h3>
<p>We may collect personal information such as your name, email address, phone number, and company details when you contact us through our website, request a quote, or subscribe to our newsletter.</p>
<h3>How We Use Your Information</h3>
<p>We use your information to respond to inquiries, provide quotations, deliver our services, send relevant updates, and improve our website experience.</p>
<h3>Contact Us</h3>
<p>For any privacy-related questions, please contact us at info@vaamtrading.com.</p>""",
     True, 1),

    ("Terms and Conditions", "terms-and-conditions",
     """<h2>Terms and Conditions</h2>
<p>These terms and conditions govern your use of the VAAM Trading website and our products and services. By using our website or purchasing our products, you agree to be bound by these terms.</p>
<h3>Products and Pricing</h3>
<p>All product prices are subject to change without notice. Prices quoted are valid for 14 days unless otherwise stated. Product availability is subject to stock levels.</p>
<h3>Warranty</h3>
<p>Product warranties are provided by the respective manufacturers. VAAM Trading assists with warranty claims but is not the direct warrantor unless explicitly stated.</p>""",
     True, 2),
]
for title, slug, content, show_footer, order in pages_data:
    Page.objects.create(
        title_en=title, slug=slug, content_en=content,
        is_published=True, show_in_footer=show_footer, order=order
    )

print()
print("=" * 50)
print("  ✓ Database seeded successfully!")
print("=" * 50)
print()
print("Summary:")
print(f"  - Site Settings: updated")
print(f"  - Hero Slides: {HeroSlide.objects.count()}")
print(f"  - Company Info: updated")
print(f"  - Company Features: {CompanyFeature.objects.count()}")
print(f"  - Statistics: {Statistic.objects.count()}")
print(f"  - Product Categories: {ProductCategory.objects.count()}")
print(f"  - Products: {Product.objects.count()}")
print(f"  - Service Categories: {ServiceCategory.objects.count()}")
print(f"  - Services: {Service.objects.count()}")
print(f"  - Process Steps: {ProcessStep.objects.count()}")
print(f"  - Project Categories: {ProjectCategory.objects.count()}")
print(f"  - Projects: {Project.objects.count()}")
print(f"  - News Categories: {NewsCategory.objects.count()}")
print(f"  - News Articles: {News.objects.count()}")
print(f"  - FAQs: {FAQ.objects.count()}")
print(f"  - Testimonials: {Testimonial.objects.count()}")
print(f"  - Brands: {Brand.objects.count()}")
print(f"  - Menus: {Menu.objects.count()}")
print(f"  - Pages: {Page.objects.count()}")
