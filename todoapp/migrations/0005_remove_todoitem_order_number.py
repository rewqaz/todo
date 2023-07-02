

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20190821_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='order_number',
        ),
    ]
