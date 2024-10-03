# Generated by Django 5.1.1 on 2024-10-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_prettynum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, verbose_name='rank'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='price',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已占用'), (2, '未使用')], default=2, verbose_name='status'),
        ),
    ]
