# Generated by Django 2.1.1 on 2018-10-04 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('quote', models.CharField(blank=True, max_length=512)),
                ('mainpic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='model_jobpic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobpic', to='info_app.model_job')),
            ],
        ),
        migrations.CreateModel(
            name='model_testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=128)),
                ('quote', models.CharField(blank=True, max_length=512)),
                ('personpic', models.ImageField(upload_to='')),
            ],
        ),
    ]