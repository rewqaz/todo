

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_auto_20190824_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
