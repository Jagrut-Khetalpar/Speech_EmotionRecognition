# Generated by Django 3.2.10 on 2022-03-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('path', models.FilePathField(default='C:\\Users\\kheta\\OneDrive\\Desktop\\new project\\Project\\media', path='C:\\Users\\kheta\\OneDrive\\Desktop\\new project\\Project\\media')),
            ],
            options={
                'unique_together': {('file', 'path')},
            },
        ),
    ]
