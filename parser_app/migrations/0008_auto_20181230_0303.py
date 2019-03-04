
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0007_resume_uploaded_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Education'),
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Skills'),
        ),
    ]