from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("portfolio_app", "0002_achievement")]

    operations = [
        migrations.AddField(model_name="education", name="cgpa", field=models.CharField(blank=True, max_length=20)),
        migrations.AddField(model_name="education", name="percentage", field=models.CharField(blank=True, max_length=20)),
    ]
