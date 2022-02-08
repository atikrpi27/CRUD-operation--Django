# Generated by Django 4.0.2 on 2022-02-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_album_table_alter_musician_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent')], default=1),
            preserve_default=False,
        ),
    ]