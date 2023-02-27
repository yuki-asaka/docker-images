import os
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        superuser = User.objects.create_superuser(
            username=username,
            email=email,
            password=password)

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
