# Generated by Django 3.1.7 on 2021-02-27 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keepnotes', '0002_checkbox_media_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkbox',
            old_name='userRef',
            new_name='noteRef',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='userRef',
            new_name='noteRef',
        ),
        migrations.AddField(
            model_name='notes',
            name='isArchived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notes',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collaberator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaberatorRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noteRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keepnotes.notes')),
            ],
        ),
    ]
