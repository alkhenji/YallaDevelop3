# Generated by Django 4.0.4 on 2022-05-30 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField()),
                ('project_owner', models.IntegerField()),
                ('username', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('mimetype', models.CharField(max_length=20)),
                ('skill', models.ManyToManyField(to='yalladevelop.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('date_completed', models.DateField(null=True)),
                ('likes', models.IntegerField(default=0)),
                ('target_money', models.IntegerField()),
                ('money_collected', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('mimetype', models.CharField(max_length=20)),
                ('funders', models.ManyToManyField(related_name='funder', to='yalladevelop.userprofile')),
                ('helpers', models.ManyToManyField(related_name='helper', to='yalladevelop.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yalladevelop.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]