# Generated by Django 3.2.11 on 2022-04-19 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_like_user_article_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recomment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.comment'),
        ),
    ]