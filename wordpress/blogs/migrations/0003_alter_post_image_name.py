# Generated by Django 5.0.7 on 2024-09-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_alter_post_image_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_name",
            field=models.ImageField(null=True, upload_to="data"),
        ),
    ]
