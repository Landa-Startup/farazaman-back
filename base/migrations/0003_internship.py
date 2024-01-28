# Generated by Django 4.2.2 on 2024-01-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_startup_logo_alter_startup_members_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=150)),
                ('cvFile', models.FileField(blank=True, null=True, upload_to='cv-files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
