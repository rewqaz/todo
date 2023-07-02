

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_todolist_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
