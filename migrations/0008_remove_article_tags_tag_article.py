# Generated by Django 5.0.3 on 2024-03-14 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_tag_article_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ForeignKey(default=str, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='api.article'),
            preserve_default=False,
        ),
    ]
