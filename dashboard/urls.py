from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Auth
    path('login/', views.dashboard_login, name='login'),
    path('logout/', views.dashboard_logout, name='logout'),

    # Dashboard
    path('', views.dashboard_home, name='home'),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # Product Categories
    path('product-categories/', views.product_category_list, name='product_category_list'),
    path('product-categories/create/', views.product_category_create, name='product_category_create'),
    path('product-categories/<int:pk>/edit/', views.product_category_edit, name='product_category_edit'),
    path('product-categories/<int:pk>/delete/', views.product_category_delete, name='product_category_delete'),

    # Services
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Service Categories
    path('service-categories/', views.service_category_list, name='service_category_list'),
    path('service-categories/create/', views.service_category_create, name='service_category_create'),
    path('service-categories/<int:pk>/edit/', views.service_category_edit, name='service_category_edit'),
    path('service-categories/<int:pk>/delete/', views.service_category_delete, name='service_category_delete'),

    # Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Project Categories
    path('project-categories/', views.project_category_list, name='project_category_list'),
    path('project-categories/create/', views.project_category_create, name='project_category_create'),
    path('project-categories/<int:pk>/edit/', views.project_category_edit, name='project_category_edit'),
    path('project-categories/<int:pk>/delete/', views.project_category_delete, name='project_category_delete'),

    # News
    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),

    # News Categories
    path('news-categories/', views.news_category_list, name='news_category_list'),
    path('news-categories/create/', views.news_category_create, name='news_category_create'),
    path('news-categories/<int:pk>/edit/', views.news_category_edit, name='news_category_edit'),
    path('news-categories/<int:pk>/delete/', views.news_category_delete, name='news_category_delete'),

    # Messages
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),

    # Hero Slides
    path('hero-slides/', views.hero_slide_list, name='hero_slide_list'),
    path('hero-slides/create/', views.hero_slide_create, name='hero_slide_create'),
    path('hero-slides/<int:pk>/edit/', views.hero_slide_edit, name='hero_slide_edit'),
    path('hero-slides/<int:pk>/delete/', views.hero_slide_delete, name='hero_slide_delete'),

    # Brands
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/create/', views.brand_create, name='brand_create'),
    path('brands/<int:pk>/edit/', views.brand_edit, name='brand_edit'),
    path('brands/<int:pk>/delete/', views.brand_delete, name='brand_delete'),

    # Company Info
    path('company-info/', views.company_info, name='company_info'),

    # Company Features
    path('features/', views.feature_list, name='feature_list'),
    path('features/create/', views.feature_create, name='feature_create'),
    path('features/<int:pk>/edit/', views.feature_edit, name='feature_edit'),
    path('features/<int:pk>/delete/', views.feature_delete, name='feature_delete'),

    # Statistics
    path('statistics/', views.statistic_list, name='statistic_list'),
    path('statistics/create/', views.statistic_create, name='statistic_create'),
    path('statistics/<int:pk>/edit/', views.statistic_edit, name='statistic_edit'),
    path('statistics/<int:pk>/delete/', views.statistic_delete, name='statistic_delete'),

    # Process Steps
    path('process-steps/', views.process_step_list, name='process_step_list'),
    path('process-steps/create/', views.process_step_create, name='process_step_create'),
    path('process-steps/<int:pk>/edit/', views.process_step_edit, name='process_step_edit'),
    path('process-steps/<int:pk>/delete/', views.process_step_delete, name='process_step_delete'),

    # Settings
    path('settings/', views.site_settings, name='site_settings'),

    # FAQs
    path('faqs/', views.faq_list, name='faq_list'),
    path('faqs/create/', views.faq_create, name='faq_create'),
    path('faqs/<int:pk>/edit/', views.faq_edit, name='faq_edit'),
    path('faqs/<int:pk>/delete/', views.faq_delete, name='faq_delete'),

    # Testimonials
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/create/', views.testimonial_create, name='testimonial_create'),
    path('testimonials/<int:pk>/edit/', views.testimonial_edit, name='testimonial_edit'),
    path('testimonials/<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),

    # Menus
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/create/', views.menu_create, name='menu_create'),
    path('menus/<int:pk>/edit/', views.menu_edit, name='menu_edit'),
    path('menus/<int:pk>/delete/', views.menu_delete, name='menu_delete'),

    # Menu Items
    path('menus/<int:menu_pk>/items/', views.menu_item_list, name='menu_item_list'),
    path('menus/<int:menu_pk>/items/create/', views.menu_item_create, name='menu_item_create'),
    path('menus/<int:menu_pk>/items/<int:pk>/edit/', views.menu_item_edit, name='menu_item_edit'),
    path('menus/<int:menu_pk>/items/<int:pk>/delete/', views.menu_item_delete, name='menu_item_delete'),

    # Pages
    path('pages/', views.page_list, name='page_list'),
    path('pages/create/', views.page_create, name='page_create'),
    path('pages/<int:pk>/edit/', views.page_edit, name='page_edit'),
    path('pages/<int:pk>/delete/', views.page_delete, name='page_delete'),

    # Countries
    path('countries/', views.country_list, name='country_list'),
    path('countries/create/', views.country_create, name='country_create'),
    path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
    path('countries/<int:pk>/delete/', views.country_delete, name='country_delete'),

    # Product Inquiries
    path('inquiries/', views.inquiry_list, name='inquiry_list'),
    path('inquiries/<int:pk>/', views.inquiry_detail, name='inquiry_detail'),
    path('inquiries/<int:pk>/delete/', views.inquiry_delete, name='inquiry_delete'),
]
