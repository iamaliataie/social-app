# Generated by Django 4.2.1 on 2023-06-08 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comment_post_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]