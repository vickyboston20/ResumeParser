
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/', verbose_name='Upload Resumes')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('mobile_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UploadResume',
        ),
    ]
