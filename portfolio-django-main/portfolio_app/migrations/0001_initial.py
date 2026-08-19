from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Profile", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=120)),
            ("role", models.CharField(default="Student Developer", max_length=160)),
            ("tagline", models.CharField(default="I build practical, modern digital experiences.", max_length=220)),
            ("about", models.TextField()),
            ("email", models.EmailField(blank=True, max_length=254)),
            ("location", models.CharField(blank=True, max_length=120)),
            ("github_url", models.URLField(blank=True)),
            ("linkedin_url", models.URLField(blank=True)),
            ("resume", models.FileField(blank=True, help_text="Upload your resume as PDF or DOCX.", null=True, upload_to="resume/")),
            ("photo", models.ImageField(blank=True, null=True, upload_to="profile/")),
        ], options={"verbose_name":"Profile","verbose_name_plural":"Profile"}),
        migrations.CreateModel(name="Skill", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=80)), ("category", models.CharField(default="Development", max_length=80)),
            ("level", models.PositiveIntegerField(default=75)), ("icon", models.CharField(blank=True, help_text="Optional icon/short label", max_length=40))
        ], options={"ordering":["category","name"]}),
        migrations.CreateModel(name="Project", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=140)), ("short_description", models.CharField(max_length=220)),
            ("description", models.TextField(blank=True)), ("technologies", models.CharField(help_text="Comma-separated technologies", max_length=250)),
            ("image", models.ImageField(blank=True, null=True, upload_to="projects/")), ("github_url", models.URLField(blank=True)),
            ("live_url", models.URLField(blank=True)), ("featured", models.BooleanField(default=True)), ("order", models.PositiveIntegerField(default=0))
        ], options={"ordering":["order","-id"]}),
        migrations.CreateModel(name="Education", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("institution", models.CharField(max_length=160)), ("degree", models.CharField(max_length=160)),
            ("field", models.CharField(blank=True, max_length=160)), ("start_year", models.PositiveIntegerField()),
            ("end_year", models.PositiveIntegerField(blank=True, null=True)), ("description", models.TextField(blank=True)),
            ("order", models.PositiveIntegerField(default=0))
        ], options={"ordering":["-start_year","order"]}),
        migrations.CreateModel(name="Certificate", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=180)), ("issuer", models.CharField(max_length=140)),
            ("issue_date", models.DateField(blank=True, null=True)), ("credential_url", models.URLField(blank=True)),
            ("image", models.ImageField(blank=True, null=True, upload_to="certificates/"))
        ], options={"ordering":["-issue_date","-id"]}),
        migrations.CreateModel(name="ContactMessage", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=120)), ("email", models.EmailField(max_length=254)),
            ("message", models.TextField()), ("created_at", models.DateTimeField(auto_now_add=True)),
            ("is_read", models.BooleanField(default=False))
        ], options={"ordering":["-created_at"]}),
    ]
