# Generated by Django 4.1.3 on 2022-12-04 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0004_alter_review_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="movie_id",
            new_name="movie",
        ),
    ]
