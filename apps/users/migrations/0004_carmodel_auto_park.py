# Generated by Django 4.1.3 on 2022-12-01 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0002_alter_autoparksmodel_table'),
        ('users', '0003_carmodel_create_at_carmodel_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparksmodel'),
            preserve_default=False,
        ),
    ]
