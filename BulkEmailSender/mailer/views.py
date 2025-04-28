from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from .models import Contact, EmailTemplate
from django.conf import settings
from django.http import HttpResponse
from django.template import Template, Context

def send_bulk_email(request):
    templates = EmailTemplate.objects.all()
    success = False

    if request.method == "POST":
        subject = request.POST.get('subject')
        plain_message = request.POST.get('message')
        template_id = request.POST.get('template_id')  # ✅ GET selected template_id
        from_email = settings.DEFAULT_FROM_EMAIL
        contacts = Contact.objects.all()

        # 1. Load template by selected ID
        try:
            template = EmailTemplate.objects.get(id=template_id)
        except EmailTemplate.DoesNotExist:
            template = None

        if template:
            template_content = template.content

            # 2. Render the template safely with context
            django_template = Template(template_content)
            context = Context({
                'subject': subject,
                'message': plain_message,
            })
            html_message = django_template.render(context)
        else:
            html_message = plain_message  # fallback

        # 3. Send email
        for contact in contacts:
            msg = EmailMultiAlternatives(subject, plain_message, from_email, [contact.email])
            msg.attach_alternative(html_message, "text/html")
            msg.send()

        success = True

    return render(request, "mailer/send_form.html", {'templates': templates, 'success': success})

def load_email_template(request):
    try:
        # 1. Get the template by name (you can change "WelcomeEmail" to whatever you want)
        templates = EmailTemplate.objects.all()
    except EmailTemplate.DoesNotExist: 
        return HttpResponse("Email template not found!")

    # 2. Get subject and content
    subject = templates.subject
    content = templates.content

    # 3. You can replace variables if you want (optional)
    content = content.replace("{{name}}", "John Doe")
    content = content.replace("{{date}}", "April 30, 2025")

    # 4. Return as HttpResponse
    return HttpResponse(f"<h1>{subject}</h1><p>{content}</p>")

def select_template_view(request):
    templates = EmailTemplate.objects.all()
    return render(request, 'mailer/send_form.html', {'templates': templates})