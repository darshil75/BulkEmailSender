# Generated by Django 5.2 on 2025-04-26 12:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0005_emailtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
