# Generated by Django 4.1.5 on 2023-04-05 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0019_message_groupchatroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='groupChatRoom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='match.groupchatroom'),
        ),
    ]
