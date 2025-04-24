from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from .models import Contact
from django.conf import settings

def send_bulk_email(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        plain_message = request.POST.get('message')
        from_email = settings.DEFAULT_FROM_EMAIL
        contacts = Contact.objects.all()

        html_message = f"""
<html>
  <body style="margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif; background-color: #f4f4f4;">
    <div style="max-width: 600px; margin: auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
      
      <!-- Header -->
      <div style="background-color: #007bff; color: white; padding: 20px; text-align: center;">
        <h1 style="margin: 0;">📬 Bulk Email Sender</h1>
        <p style="margin: 5px 0 0;">Reach your audience with ease</p>
      </div>

      <!-- Body -->
      <div style="padding: 30px;">
        <h2 style="color: #333;">{subject}</h2>
        <p style="font-size: 16px; color: #555; line-height: 1.6;">
          {plain_message}
        </p>

        <div style="margin-top: 30px; text-align: center;">
          <a href="https://yourwebsite.com" style="background-color: #28a745; color: white; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 5px;">
            Learn More
          </a>
        </div>
      </div>

      <!-- Footer -->
      <div style="background-color: #f1f1f1; color: #888; text-align: center; padding: 15px; font-size: 12px;">
        You received this email because you're subscribed to our mailing list.<br>
        <a href="https://yourwebsite.com/unsubscribe" style="color: #007bff;">Unsubscribe</a>
      </div>
    </div>
  </body>
</html>
"""



        for contact in contacts:
            msg = EmailMultiAlternatives(subject, plain_message, from_email, [contact.email])
            msg.attach_alternative(html_message, "text/html")
            msg.send()

        return render(request, "mailer/send_form.html", {"success": True})

    return render(request, "mailer/send_form.html")