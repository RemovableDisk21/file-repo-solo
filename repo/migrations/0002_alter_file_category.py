# Generated by Django 4.0.1 on 2022-02-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='category',
            field=models.CharField(choices=[('video', 'Video'), ('text', 'Text'), ('image', 'Image'), ('executable', 'Executable'), ('document', 'Document'), ('audio', 'Audio'), ('compressed', 'Compressed'), ('others', 'Others')], max_length=64),
        ),
    ]
