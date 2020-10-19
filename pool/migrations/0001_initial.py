# Generated by Django 3.1.1 on 2020-09-27 21:24

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
            name='PoolTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=12)),
                ('feedback_img', models.ImageField(upload_to='')),
                ('feedback_img_phash', models.CharField(max_length=16, unique=True)),
                ('feedback_img_chash', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.CharField(max_length=9)),
                ('revealed', models.BooleanField(default=False)),
                ('reveal_date', models.DateTimeField(blank=True, null=True)),
                ('is_precog', models.BooleanField()),
                ('allowed_categories', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now=True)),
                ('pool_target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pool.pooltarget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now=True)),
                ('moderated', models.BooleanField(default=False)),
                ('moderated_date', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('rejection_reason', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(max_length=12)),
                ('description', models.TextField()),
                ('moderated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderator', to=settings.AUTH_USER_MODEL)),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['submission_date'],
            },
        ),
        migrations.AddField(
            model_name='pooltarget',
            name='submission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pool.submission'),
        ),
    ]
