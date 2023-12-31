# Generated by Django 4.2.2 on 2023-07-02 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('correct_choice', models.CharField(max_length=100)),
                ('refid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
