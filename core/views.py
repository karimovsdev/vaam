import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .models import (
    SiteSettings, HeroSlide, CompanyInfo, CompanyFeature, Statistic,
    Certificate, TeamMember, ProductCategory, Product,
    ServiceCategory, Service, ProcessStep,
    ProjectCategory, Project, NewsCategory, News,
    FAQ, Testimonial, Brand, ContactMessage, Page,
    Country, ProductInquiry
)
from .forms import ContactMessageForm, ProductInquiryForm


def home(request):
    slides = HeroSlide.objects.filter(is_active=True)
    slides_json = json.dumps([
        {
            'img': slide.image.url if slide.image else '',
            'sub': slide.subtitle or '',
            'title': slide.title,
            'text': slide.description or '',
            'b1': {'t': slide.button1_text or 'Learn More', 'h': slide.button1_url or reverse('core:products')},
            'b2': {'t': slide.button2_text or 'Contact Us', 'h': slide.button2_url or reverse('core:contact')},
        }
        for slide in slides
    ])
    try:
        company_info = CompanyInfo.objects.get(pk=1)
    except CompanyInfo.DoesNotExist:
        company_info = None

    context = {
        'active_page': 'home',
        'slides': slides,
        'slides_json': slides_json,
        'company_info': company_info,
        'features': CompanyFeature.objects.filter(is_active=True)[:4],
        'services': Service.objects.filter(is_active=True)[:3],
        'process_steps': ProcessStep.objects.filter(is_active=True)[:4],
        'statistics': Statistic.objects.filter(is_active=True)[:4],
        'featured_projects': Project.objects.filter(is_active=True, is_featured=True)[:3],
        'latest_news': News.objects.filter(is_published=True)[:3],
        'brands': Brand.objects.filter(is_active=True),
        'countries': Country.objects.filter(is_active=True),
        'product_categories': ProductCategory.objects.filter(is_active=True),
        'inquiry_form': ProductInquiryForm(),
    }
    return render(request, 'core/home.html', context)


def about(request):
    try:
        company_info = CompanyInfo.objects.get(pk=1)
    except CompanyInfo.DoesNotExist:
        company_info = None

    context = {
        'active_page': 'about',
        'company_info': company_info,
        'features': CompanyFeature.objects.filter(is_active=True),
        'statistics': Statistic.objects.filter(is_active=True),
        'certificates': Certificate.objects.all(),
        'team_members': TeamMember.objects.filter(is_active=True),
        'brands': Brand.objects.filter(is_active=True),
    }
    return render(request, 'core/about.html', context)


def services(request):
    context = {
        'active_page': 'services',
        'services': Service.objects.filter(is_active=True),
        'process_steps': ProcessStep.objects.filter(is_active=True),
        'faqs': FAQ.objects.filter(is_active=True),
    }
    return render(request, 'core/services.html', context)


def products(request):
    categories = ProductCategory.objects.filter(is_active=True)
    active_category = request.GET.get('category', '')
    product_list = Product.objects.filter(is_active=True).select_related('category')
    if active_category:
        product_list = product_list.filter(category__slug=active_category)

    paginator = Paginator(product_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'active_page': 'products',
        'categories': categories,
        'products': page_obj,
        'active_category': active_category,
        'page_obj': page_obj,
    }
    return render(request, 'core/products.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:3]

    context = {
        'active_page': 'products',
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'core/product_detail.html', context)


def projects(request):
    categories = ProjectCategory.objects.filter(is_active=True)
    active_category = request.GET.get('category', '')
    project_list = Project.objects.filter(is_active=True).select_related('category')
    if active_category:
        project_list = project_list.filter(category__slug=active_category)

    paginator = Paginator(project_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'active_page': 'projects',
        'categories': categories,
        'projects': page_obj,
        'active_category': active_category,
        'page_obj': page_obj,
    }
    return render(request, 'core/projects.html', context)


def news_list(request):
    articles = News.objects.filter(is_published=True).select_related('category')
    categories = NewsCategory.objects.filter(is_active=True)
    active_category = request.GET.get('category', '')
    if active_category:
        articles = articles.filter(category__slug=active_category)

    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'active_page': 'news',
        'articles': page_obj,
        'categories': categories,
        'active_category': active_category,
        'page_obj': page_obj,
    }
    return render(request, 'core/news.html', context)


def news_detail(request, slug):
    article = get_object_or_404(News, slug=slug, is_published=True)
    related_articles = News.objects.filter(is_published=True).exclude(pk=article.pk)[:3]

    context = {
        'active_page': 'news',
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'core/news_detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been sent successfully! We will get back to you soon.'))
            return redirect('core:contact')
    else:
        form = ContactMessageForm()

    context = {
        'active_page': 'contact',
        'form': form,
        'testimonials': Testimonial.objects.filter(is_active=True),
        'faqs': FAQ.objects.filter(is_active=True),
    }
    return render(request, 'core/contact.html', context)


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    context = {
        'active_page': f'page_{page.slug}',
        'page': page,
    }
    return render(request, 'core/page_detail.html', context)


def product_inquiry(request):
    """Handle product sourcing inquiry form submission."""
    if request.method == 'POST':
        form = ProductInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your product inquiry has been submitted successfully! Our team will review your request and contact you shortly.'))
            return redirect('core:home')
        else:
            messages.error(request, _('Please correct the errors below.'))
    else:
        form = ProductInquiryForm()

    context = {
        'active_page': 'inquiry',
        'form': form,
        'product_categories': ProductCategory.objects.filter(is_active=True),
    }
    return render(request, 'core/product_inquiry.html', context)
