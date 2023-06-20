# Generated by Django 4.2.1 on 2023-06-06 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_rename_movie_review_offer_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='firm',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='Ocenjeni', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ocenjivac', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
