# Generated by Django 3.0.3 on 2020-03-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_auto_20200302_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='status',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=10, verbose_name='status'),
        ),
    ]