# Generated by Django 5.1.3 on 2024-11-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('Customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Customer_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('Customer_age', models.IntegerField()),
                ('Loan_Amount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
