

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0016_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='hasItem',
            field=models.BooleanField(default=False),
        ),
    ]
