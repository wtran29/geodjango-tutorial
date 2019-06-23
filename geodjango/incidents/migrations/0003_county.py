# Generated by Django 2.2.2 on 2019-06-23 00:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0002_auto_20190622_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statefp', models.CharField(max_length=2)),
                ('countyfp', models.CharField(max_length=3)),
                ('countyns', models.CharField(max_length=8)),
                ('geoid', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('namelsad', models.CharField(max_length=100)),
                ('lsad', models.CharField(max_length=2)),
                ('classfp', models.CharField(max_length=2)),
                ('mtfcc', models.CharField(max_length=5)),
                ('csafp', models.CharField(max_length=3)),
                ('cbsafp', models.CharField(max_length=5)),
                ('metdivfp', models.CharField(max_length=5)),
                ('funcstat', models.CharField(max_length=1)),
                ('aland', models.BigIntegerField()),
                ('awater', models.BigIntegerField()),
                ('intptlat', models.CharField(max_length=11)),
                ('intptlon', models.CharField(max_length=12)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
        ),
    ]