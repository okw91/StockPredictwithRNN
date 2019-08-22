# Generated by Django 2.1.2 on 2018-10-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_server', '0003_a000100'),
    ]

    operations = [
        migrations.CreateModel(
            name='A000640',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a000640',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A001630',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a001630',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A006280',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a006280',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A008930',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a008930',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A009290',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a009290',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A069620',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a069620',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A096760',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a096760',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A128940',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a128940',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='A249420',
            fields=[
                ('stock_index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stock_date', models.BigIntegerField(blank=True, null=True)),
                ('stock_time', models.BigIntegerField(blank=True, null=True)),
                ('stock_price', models.BigIntegerField(blank=True, null=True)),
                ('stock_volume', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a249420',
                'managed': False,
            },
        ),
    ]