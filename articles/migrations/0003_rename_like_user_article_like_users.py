# Generated by Django 3.2.11 on 2022-04-19 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_like_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='like_user',
            new_name='like_users',
        ),
    ]