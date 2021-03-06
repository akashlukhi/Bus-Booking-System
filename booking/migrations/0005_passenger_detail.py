# Generated by Django 3.0.2 on 2020-03-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_bus_info_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='passenger_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('age', models.IntegerField()),
                ('zender', models.CharField(max_length=5)),
                ('booked_by', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('bus_plate_no', models.CharField(max_length=13)),
                ('bus_name', models.CharField(max_length=50)),
            ],
        ),
    ]
