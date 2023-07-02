

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_auto_20190824_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='time_to_do',
            field=models.DateTimeField(),
        ),
    ]
