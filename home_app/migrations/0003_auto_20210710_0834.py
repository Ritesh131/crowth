# Generated by Django 3.2.4 on 2021-07-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_auto_20210703_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='query',
            name='company_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='monthly_pay',
            field=models.CharField(choices=[('1', '$3-5k per Month'), ('2', '$5-10k per Month'), ('3', '$10-20k per Month'), ('4', '$20k+ per Month')], default='1', max_length=150),
        ),
        migrations.AlterField(
            model_name='query',
            name='message',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='services',
            field=models.ManyToManyField(blank=True, to='home_app.Services'),
        ),
    ]