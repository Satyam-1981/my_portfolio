# Student Portfolio — Django

A simple student portfolio built with Django, HTML, CSS and a small amount of JavaScript.

## Sections
- Hero
- About Me
- Education History
- Skills
- Projects Showcase
- Certificates
- Contact

## Features
- Django-powered content management through the admin panel
- Responsive modern UI
- Dark/light theme toggle
- Small hero/card/button animations
- Project, skill, education and certificate management
- Contact form saved to the database
- Email notification sent to the portfolio owner
- Confirmation email sent to the visitor
- Resume upload/download support (PDF or DOCX)
- SQLite for local development
- Supabase PostgreSQL for production database
- Supabase Storage for persistent uploaded files

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Website: https://my-portfolio-hxbi.onrender.com/

## Add content
Use Django Admin to add projects, skills, education entries and certificates.

Upload your resume from Django Admin → Profile. Supported formats are PDF and DOCX. Uploaded files are stored locally during development and in Supabase Storage in production.

## Design
The frontend intentionally uses a simple, clean one-page layout suitable for a first student portfolio: plain CSS, no frontend framework, and no unnecessary animations or JavaScript.

## Contact Form

When someone submits the form:
1. The message is saved in Django Admin → Contact messages.
2. You receive the message by email.
3. The sender receives a confirmation email.

For Gmail, set these environment variables before running the project:

- `EMAIL_HOST_USER` — your Gmail address
- `EMAIL_HOST_PASSWORD` — your Gmail App Password

Do not use your normal Gmail password or commit it to GitHub.


## Deployment

Production uses **Render** for the Django web service, **Supabase PostgreSQL** for the database, and **Supabase Storage** for uploaded files.

Set these environment variables in Render:

- `SECRET_KEY` — a long random secret
- `DEBUG` — `False`
- `ALLOWED_HOSTS` — your Render hostname, for example `your-app.onrender.com`
- `CSRF_TRUSTED_ORIGINS` — your HTTPS Render URL, for example `https://your-app.onrender.com`
- `DATABASE_URL` — the Supabase PostgreSQL connection string
- `SUPABASE_STORAGE_ENABLED` — `True`
- `SUPABASE_STORAGE_BUCKET` — your public Supabase Storage bucket name, for example `portfolio`
- `SUPABASE_S3_ENDPOINT` — your Supabase S3 endpoint, for example `https://<project-ref>.storage.supabase.co/storage/v1/s3`
- `SUPABASE_S3_REGION` — the region shown in Supabase Storage S3 settings
- `SUPABASE_S3_ACCESS_KEY` — the generated Supabase S3 access key
- `SUPABASE_S3_SECRET_KEY` — the generated Supabase S3 secret key
- `SUPABASE_STORAGE_PUBLIC_URL` — the public bucket URL prefix, for example `https://<project-ref>.supabase.co/storage/v1/object/public/portfolio`
- `EMAIL_HOST_USER` — your Gmail address (optional)
- `EMAIL_HOST_PASSWORD` — your Gmail App Password (optional)
- `DEFAULT_FROM_EMAIL` — usually the same Gmail address (optional)

Render build command:

```text
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

Render start command:

```text
gunicorn portfolio_project.wsgi:application
```

Do not commit `.env`. It is ignored by `.gitignore`.
