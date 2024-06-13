# Generated by Django 5.0.6 on 2024-06-01 13:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_pages", "0005_dars_likes"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="comment",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="user",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="news",
        ),
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="comment",
            name="dars",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="app_pages.dars",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="app_pages.comment",
            ),
        ),
    ]
