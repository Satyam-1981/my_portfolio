from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=160, default="Student Developer")
    tagline = models.CharField(max_length=220, default="I build practical, modern digital experiences.")
    about = models.TextField()
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True, help_text="Upload your resume as PDF or DOCX.")
    photo = models.ImageField(upload_to="profile/", blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80, default="Development")
    level = models.PositiveIntegerField(default=75)
    icon = models.CharField(max_length=40, blank=True, help_text="Optional icon/short label")

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=140)
    short_description = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=250, help_text="Comma-separated technologies")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=160)
    degree = models.CharField(max_length=160)
    field = models.CharField(max_length=160, blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-start_year", "order"]

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Certificate(models.Model):
    title = models.CharField(max_length=180)
    issuer = models.CharField(max_length=140)
    issue_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="certificates/", blank=True, null=True)

    class Meta:
        ordering = ["-issue_date", "-id"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"
