# Generated by Django 5.0.1 on 2024-02-10 17:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('01d98200-3f99-4121-b267-4f8043ea84ae'), editable=False, primary_key=True, serialize=False),
        ),
    ]