# VAAM Project - Comprehensive Audit Plan

## Project: VAAM Import and Export Trading Co., LTD
## Date: 2026-02-09
## Stack: Django 5.x + modeltranslation + Tailwind CSS (CDN) + Alpine.js + SQLite

---

## 1. BACKEND AUDIT

### 1.1 Security Issues
- [x] **SEC-01**: SECRET_KEY hardcoded in settings.py — move to environment variables
- [x] **SEC-02**: DEBUG = True hardcoded — use env variable
- [x] **SEC-03**: ALLOWED_HOSTS = ['*'] — restrict to actual domains
- [x] **SEC-04**: Logout via GET request (CSRF vulnerability) — change to POST
- [x] **SEC-05**: No SECURE_* settings for production (HSTS, secure cookies, etc.)

### 1.2 Views Issues
- [x] **VIEW-01**: Contact success message not translatable — wrap in gettext_lazy
- [x] **VIEW-02**: Hero slide button URLs hardcoded in JSON ('/products/', '/contact/') — use reverse()
- [x] **VIEW-03**: CompanyInfo.objects.get(pk=1) — use singleton pattern consistently
- [x] **VIEW-04**: No pagination on list views (products, projects, news)

### 1.3 Forms Issues
- [x] **FORM-01**: ContactMessage form success message not wrapped in translation

### 1.4 URL Configuration
- [x] **URL-01**: Admin redirect should use proper redirect view, not lambda

---

## 2. DATABASE AUDIT

### 2.1 Model Issues
- [x] **DB-01**: Product.get_absolute_url() missing — needed for SEO/admin
- [x] **DB-02**: News.get_absolute_url() missing — needed for SEO
- [x] **DB-03**: Project.get_absolute_url() missing
- [x] **DB-04**: Service.get_absolute_url() missing
- [x] **DB-05**: No database indexes on frequently queried fields (slug, is_active, is_published)
- [x] **DB-06**: ContactMessage missing __str__ with full_name property usage

---

## 3. FRONTEND AUDIT

### 3.1 SEO Issues
- [x] **SEO-01**: No Open Graph meta tags (og:title, og:description, og:image, og:url)
- [x] **SEO-02**: No Twitter Card meta tags
- [x] **SEO-03**: No canonical URL tag
- [x] **SEO-04**: Product detail pages missing meta_description block override
- [x] **SEO-05**: News detail pages missing proper meta tags
- [x] **SEO-06**: No structured data (JSON-LD) for Organization

### 3.2 Broken Links
- [x] **LINK-01**: Privacy Policy footer link is # — link to pages or remove
- [x] **LINK-02**: Terms footer link is # — link to pages or remove
- [x] **LINK-03**: Social share URLs not URL-encoding article titles

### 3.3 Missing Translations in Templates
- [x] **TRANS-01**: "25+" hardcoded in home.html
- [x] **TRANS-02**: Default fallback strings not wrapped in {% trans %}
- [x] **TRANS-03**: Various hardcoded English strings in templates

---

## 4. ACCESSIBILITY AUDIT

- [x] **A11Y-01**: Flag images have empty alt="" — add descriptive alt text
- [x] **A11Y-02**: Hamburger menu button missing aria-label
- [x] **A11Y-03**: WhatsApp floating button missing aria-label
- [x] **A11Y-04**: Scroll-to-top button missing aria-label
- [x] **A11Y-05**: Hero slider prev/next buttons missing aria-label
- [x] **A11Y-06**: Slider dot buttons missing aria-label
- [x] **A11Y-07**: Google Maps iframe missing title attribute (contact.html)
- [x] **A11Y-08**: No fallback image/placeholder when images are missing

---

## 5. RTL SUPPORT AUDIT

- [x] **RTL-01**: No Arabic-specific font loaded (needs Cairo/Tajawal/Noto Sans Arabic)
- [x] **RTL-02**: Manual CSS overrides are incomplete — many directional utilities not covered
- [x] **RTL-03**: Service alternating layout causes double-reversal in RTL

---

## 6. TRANSLATION AUDIT

- [x] **I18N-01**: locale/tr/ contains AZERBAIJANI, not Turkish — CRITICAL BUG
- [x] **I18N-02**: locale/en/ has no .po file — needs generation
- [x] **I18N-03**: Dashboard (admin panel) has ZERO i18n support
- [x] **I18N-04**: Contact form success message not translatable
- [x] **I18N-05**: .po files missing proper headers

---

## 7. DASHBOARD (ADMIN PANEL) AUDIT

- [x] **DASH-01**: No {% load i18n %} — entire dashboard is English-only
- [x] **DASH-02**: <html lang="en"> hardcoded
- [x] **DASH-03**: Mobile sidebar missing items and active states
- [x] **DASH-04**: Search input in header has no functionality
- [x] **DASH-05**: Footer copyright hardcoded year 2026 — use {% now "Y" %}
- [x] **DASH-06**: Login page logo links to # — should link to home
- [x] **DASH-07**: Login page hardcoded copyright year

---

## 8. PERFORMANCE AUDIT

- [x] **PERF-01**: Tailwind CSS via CDN — not production-ready
- [x] **PERF-02**: Alpine.js loaded with unpinned @3.x.x version
- [x] **PERF-03**: Font Awesome CDN missing integrity/crossorigin
- [x] **PERF-04**: No image lazy loading
- [x] **PERF-05**: No CSS/JS minification strategy
- [x] **PERF-06**: context_processors.py loads all menus/services on every request

---

## 9. UX/UI & RESPONSIVENESS AUDIT

- [x] **UX-01**: Top bar hidden on tablets (hidden lg:block) — no medium breakpoint
- [x] **UX-02**: Mobile nav overlay top-[72px] is hardcoded
- [x] **UX-03**: Missing product/project image fallbacks
- [x] **UX-04**: No loading states on forms
- [x] **UX-05**: FAQ accordion missing aria-expanded attribute

---

## 10. ADMIN-FRONTEND CONNECTION AUDIT

- [x] **CONN-01**: admin.py uses basic register() — no ModelAdmin customization
- [x] **CONN-02**: No image preview in admin forms
- [x] **CONN-03**: No ordering or filtering in admin
