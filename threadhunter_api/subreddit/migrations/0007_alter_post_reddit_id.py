# Generated by Django 5.0.9 on 2024-12-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0006_alter_post_reddit_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reddit_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
