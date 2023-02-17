# Generated by Django 4.1.6 on 2023-02-17 12:26

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user_gender_user_image_user_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]