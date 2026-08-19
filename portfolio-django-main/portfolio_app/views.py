from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import Certificate, ContactMessage, Education, Profile, Project, Skill


def home(request):
    return render(request, "portfolio_app/home.html", {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.filter(featured=True),
        "education": Education.objects.all(),
        "certificates": Certificate.objects.all(),
    })


def contact(request):
    if request.method != "POST":
        return redirect("portfolio:home")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not message:
        messages.error(request, "Please fill in all fields.")
        return redirect("portfolio:home")

    ContactMessage.objects.create(
        name=name,
        email=email,
        message=message,
    )

    try:
        owner_email = settings.EMAIL_HOST_USER
        sender_name = Profile.objects.values_list("name", flat=True).first() or "Portfolio Owner"

        if not owner_email or not settings.DEFAULT_FROM_EMAIL:
            messages.warning(
                request,
                "Your message was saved, but email notifications are not configured yet."
            )
            return redirect("portfolio:home")

        # Send the visitor's message to you.
        send_mail(
            subject=f"New portfolio message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[owner_email],
            fail_silently=False,
        )

        # Send a confirmation to the visitor.
        send_mail(
            subject="Thanks for contacting me",
            message=(
                f"Hi {name},\n\n"
                f"Thank you for contacting {sender_name}. "
                "Your message has been received. I will get back to you soon.\n\n"
                "Your message:\n"
                f"{message}\n\n"
                "Best regards,\n"
                f"{sender_name}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Message sent! A confirmation email was sent to you.")
    except Exception as e:
        print(f"SMTP EMAIL ERROR:{e!r}",flush=True)
        messages.warning(
            request,
            "Your message was saved, but the email could not be sent. Check the SMTP settings."
        )

    return redirect("portfolio:home")
