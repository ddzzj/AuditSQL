# Generated by Django 2.0.2 on 2018-05-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0010_incepmakeexectask_rollback_sqlsha1'),
    ]

    operations = [
        migrations.AddField(
            model_name='inceptionhostconfig',
            name='purpose',
            field=models.CharField(choices=[('0', '审核'), ('1', '查询')], default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='incepmakeexectask',
            name='rollback_sqlsha1',
            field=models.CharField(default='', max_length=120, verbose_name='rollback sqlsha1'),
        ),
    ]