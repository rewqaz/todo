

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_remove_todoitem_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
