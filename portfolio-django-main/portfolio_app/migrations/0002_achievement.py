from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("portfolio_app", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Achievement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("description", models.TextField(blank=True)),
                ("icon", models.CharField(blank=True, default="✦", max_length=24)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        )
    ]
