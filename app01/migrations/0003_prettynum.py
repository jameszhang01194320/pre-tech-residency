# Generated by Django 3.2.9 on 2021-11-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20211126_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='mobile_num')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('level', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, verbose_name='level')),
                ('status', models.SmallIntegerField(choices=[(1, 'used'), (2, 'unuse')], default=2, verbose_name='status')),
            ],
        ),
    ]
