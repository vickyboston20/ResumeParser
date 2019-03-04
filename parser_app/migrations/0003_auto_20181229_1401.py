
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0002_auto_20181229_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
    ]
