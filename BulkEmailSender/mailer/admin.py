from django.contrib import admin
from .models import Contact, EmailTemplate

admin.site.register(Contact)

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')