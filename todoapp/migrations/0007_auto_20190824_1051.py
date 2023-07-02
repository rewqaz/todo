
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_todoitem_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='time_to_do',
            field=models.DateField(),
        ),
    ]
