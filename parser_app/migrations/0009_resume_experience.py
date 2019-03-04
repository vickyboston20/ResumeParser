
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0008_auto_20181230_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Experience'),
        ),
    ]