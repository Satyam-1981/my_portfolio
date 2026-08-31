from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Achievement, Certificate, Education, Profile, Project, Skill


def home(request):
    skills = list(Skill.objects.all())
    grouped_skills = {}
    for skill in skills:
        grouped_skills.setdefault(skill.category, []).append(skill)

    return render(request, "portfolio_app/home.html", {
        "profile": Profile.objects.first(),
        "skill_groups": grouped_skills.items(),
        "projects": Project.objects.filter(featured=True),
        "education": Education.objects.all(),
        "certificates": Certificate.objects.all(),
        "achievements": Achievement.objects.all(),
        "contact_form": ContactForm(),
    })


def contact(request):
    if request.method != "POST":
        return redirect("portfolio:home")

    form = ContactForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Please enter a valid name, email address and message.")
        return redirect("portfolio:home#contact")

    with transaction.atomic():
        contact_message = form.save()

    try:
        owner_email = settings.EMAIL_HOST_USER
        sender_name = Profile.objects.values_list("name", flat=True).first() or "Portfolio Owner"
        if owner_email and settings.DEFAULT_FROM_EMAIL:
            send_mail(
                subject=f"New portfolio message from {contact_message.name}",
                message=f"Name: {contact_message.name}\nEmail: {contact_message.email}\n\nMessage:\n{contact_message.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[owner_email],
                fail_silently=False,
            )
            send_mail(
                subject="Thanks for contacting me",
                message=f"Hi {contact_message.name},\n\nThank you for contacting {sender_name}. Your message has been received.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_message.email],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully. I'll get back to you soon.")
        else:
            messages.success(request, "Message saved successfully. I'll get back to you soon.")
    except Exception:
        messages.success(request, "Message saved successfully. I'll get back to you soon.")

    return redirect("portfolio:home#contact")
