# Generated by Django 3.2.9 on 2021-12-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('answer_id', models.IntegerField()),
            ],
        ),
    ]
