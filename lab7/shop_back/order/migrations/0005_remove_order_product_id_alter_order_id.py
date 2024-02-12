# Generated by Django 5.0.1 on 2024-02-10 17:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('03923f9b-8d28-4377-9e31-d200faaf66c0'), editable=False, primary_key=True, serialize=False),
        ),
    ]