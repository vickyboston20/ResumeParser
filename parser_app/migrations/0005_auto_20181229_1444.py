
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0004_auto_20181229_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
    ]
