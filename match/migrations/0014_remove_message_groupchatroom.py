# Generated by Django 4.1.5 on 2023-04-05 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0013_alter_message_groupchatroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='groupChatRoom',
        ),
    ]
