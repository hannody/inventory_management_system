# Generated by Django 3.2.9 on 2021-12-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_supplier_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='notes',
            new_name='note',
        ),
        migrations.AddField(
            model_name='item',
            name='availability',
            field=models.BooleanField(default=False),
        ),
    ]
