# Generated by Django 3.2 on 2022-08-29 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.photo')),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
    ]
