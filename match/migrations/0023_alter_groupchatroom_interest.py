# Generated by Django 4.2.1 on 2023-06-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0022_participant_groupchatroom_alter_participant_chatroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchatroom',
            name='interest',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
