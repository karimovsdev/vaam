"""
Migration to rename all _tr (Turkish) fields to _az (Azerbaijani).
The locale/tr/ translations were actually Azerbaijani, not Turkish.
This migration renames all modeltranslation _tr columns to _az.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_menu_page_menuitem'),
    ]

    operations = [
        # Brand
        migrations.RenameField(model_name='brand', old_name='name_tr', new_name='name_az'),

        # Certificate
        migrations.RenameField(model_name='certificate', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='certificate', old_name='title_tr', new_name='title_az'),

        # CompanyFeature
        migrations.RenameField(model_name='companyfeature', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='companyfeature', old_name='title_tr', new_name='title_az'),

        # CompanyInfo
        migrations.RenameField(model_name='companyinfo', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='companyinfo', old_name='history_tr', new_name='history_az'),
        migrations.RenameField(model_name='companyinfo', old_name='mission_tr', new_name='mission_az'),
        migrations.RenameField(model_name='companyinfo', old_name='subtitle_tr', new_name='subtitle_az'),
        migrations.RenameField(model_name='companyinfo', old_name='title_tr', new_name='title_az'),
        migrations.RenameField(model_name='companyinfo', old_name='values_tr', new_name='values_az'),
        migrations.RenameField(model_name='companyinfo', old_name='vision_tr', new_name='vision_az'),

        # FAQ
        migrations.RenameField(model_name='faq', old_name='answer_tr', new_name='answer_az'),
        migrations.RenameField(model_name='faq', old_name='question_tr', new_name='question_az'),

        # HeroSlide
        migrations.RenameField(model_name='heroslide', old_name='button1_text_tr', new_name='button1_text_az'),
        migrations.RenameField(model_name='heroslide', old_name='button2_text_tr', new_name='button2_text_az'),
        migrations.RenameField(model_name='heroslide', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='heroslide', old_name='subtitle_tr', new_name='subtitle_az'),
        migrations.RenameField(model_name='heroslide', old_name='title_tr', new_name='title_az'),

        # News
        migrations.RenameField(model_name='news', old_name='author_tr', new_name='author_az'),
        migrations.RenameField(model_name='news', old_name='content_tr', new_name='content_az'),
        migrations.RenameField(model_name='news', old_name='meta_description_tr', new_name='meta_description_az'),
        migrations.RenameField(model_name='news', old_name='meta_title_tr', new_name='meta_title_az'),
        migrations.RenameField(model_name='news', old_name='summary_tr', new_name='summary_az'),
        migrations.RenameField(model_name='news', old_name='title_tr', new_name='title_az'),

        # NewsCategory
        migrations.RenameField(model_name='newscategory', old_name='name_tr', new_name='name_az'),

        # ProcessStep
        migrations.RenameField(model_name='processstep', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='processstep', old_name='title_tr', new_name='title_az'),

        # Product
        migrations.RenameField(model_name='product', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='product', old_name='meta_description_tr', new_name='meta_description_az'),
        migrations.RenameField(model_name='product', old_name='meta_title_tr', new_name='meta_title_az'),
        migrations.RenameField(model_name='product', old_name='name_tr', new_name='name_az'),
        migrations.RenameField(model_name='product', old_name='short_description_tr', new_name='short_description_az'),

        # ProductCategory
        migrations.RenameField(model_name='productcategory', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='productcategory', old_name='name_tr', new_name='name_az'),

        # ProductImage
        migrations.RenameField(model_name='productimage', old_name='alt_text_tr', new_name='alt_text_az'),

        # ProductSpecification
        migrations.RenameField(model_name='productspecification', old_name='key_tr', new_name='key_az'),
        migrations.RenameField(model_name='productspecification', old_name='value_tr', new_name='value_az'),

        # Project
        migrations.RenameField(model_name='project', old_name='client_tr', new_name='client_az'),
        migrations.RenameField(model_name='project', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='project', old_name='location_tr', new_name='location_az'),
        migrations.RenameField(model_name='project', old_name='short_description_tr', new_name='short_description_az'),
        migrations.RenameField(model_name='project', old_name='title_tr', new_name='title_az'),

        # ProjectCategory
        migrations.RenameField(model_name='projectcategory', old_name='name_tr', new_name='name_az'),

        # Service
        migrations.RenameField(model_name='service', old_name='description_tr', new_name='description_az'),
        migrations.RenameField(model_name='service', old_name='features_tr', new_name='features_az'),
        migrations.RenameField(model_name='service', old_name='short_description_tr', new_name='short_description_az'),
        migrations.RenameField(model_name='service', old_name='title_tr', new_name='title_az'),

        # ServiceCategory
        migrations.RenameField(model_name='servicecategory', old_name='name_tr', new_name='name_az'),

        # SiteSettings
        migrations.RenameField(model_name='sitesettings', old_name='address_tr', new_name='address_az'),
        migrations.RenameField(model_name='sitesettings', old_name='address2_tr', new_name='address2_az'),
        migrations.RenameField(model_name='sitesettings', old_name='meta_description_tr', new_name='meta_description_az'),
        migrations.RenameField(model_name='sitesettings', old_name='meta_keywords_tr', new_name='meta_keywords_az'),
        migrations.RenameField(model_name='sitesettings', old_name='meta_title_tr', new_name='meta_title_az'),
        migrations.RenameField(model_name='sitesettings', old_name='site_description_tr', new_name='site_description_az'),
        migrations.RenameField(model_name='sitesettings', old_name='site_name_tr', new_name='site_name_az'),
        migrations.RenameField(model_name='sitesettings', old_name='working_hours_tr', new_name='working_hours_az'),

        # Statistic
        migrations.RenameField(model_name='statistic', old_name='title_tr', new_name='title_az'),

        # TeamMember
        migrations.RenameField(model_name='teammember', old_name='bio_tr', new_name='bio_az'),
        migrations.RenameField(model_name='teammember', old_name='name_tr', new_name='name_az'),
        migrations.RenameField(model_name='teammember', old_name='position_tr', new_name='position_az'),

        # Testimonial
        migrations.RenameField(model_name='testimonial', old_name='company_tr', new_name='company_az'),
        migrations.RenameField(model_name='testimonial', old_name='content_tr', new_name='content_az'),
        migrations.RenameField(model_name='testimonial', old_name='name_tr', new_name='name_az'),
        migrations.RenameField(model_name='testimonial', old_name='position_tr', new_name='position_az'),

        # Menu (from migration 0003)
        migrations.RenameField(model_name='menu', old_name='title_tr', new_name='title_az'),

        # MenuItem (from migration 0003)
        migrations.RenameField(model_name='menuitem', old_name='title_tr', new_name='title_az'),

        # Page (from migration 0003)
        migrations.RenameField(model_name='page', old_name='title_tr', new_name='title_az'),
        migrations.RenameField(model_name='page', old_name='content_tr', new_name='content_az'),
        migrations.RenameField(model_name='page', old_name='excerpt_tr', new_name='excerpt_az'),
        migrations.RenameField(model_name='page', old_name='meta_title_tr', new_name='meta_title_az'),
        migrations.RenameField(model_name='page', old_name='meta_description_tr', new_name='meta_description_az'),
    ]
