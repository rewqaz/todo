

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0014_todolist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='user',
        ),
        migrations.DeleteModel(
            name='ToDoUser',
        ),
    ]
