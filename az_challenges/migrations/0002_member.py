# Generated by Django 2.0.6 on 2018-06-12 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('az_challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('challenge_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='az_challenges.ChallengeGroup')),
            ],
        ),
    ]
