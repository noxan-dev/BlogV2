# Generated by Django 4.0.6 on 2022-08-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_options_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
