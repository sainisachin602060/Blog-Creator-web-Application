# Generated by Django 4.1.3 on 2023-04-26 10:12

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DecodeApp', '0005_querysend'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Catogery',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='postedDate',
            field=models.DateField(default=datetime.date(2023, 4, 26)),
        ),
    ]
