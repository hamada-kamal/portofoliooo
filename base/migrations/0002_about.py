# Generated by Django 3.1.7 on 2021-06-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brief', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=11)),
                ('address', models.CharField(max_length=20)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('whatsapp_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('linked_in_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('job', models.ManyToManyField(to='base.Job')),
            ],
        ),
    ]
