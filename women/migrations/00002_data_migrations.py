from django.db import migrations, models


def add_initial_data(apps, schema_editor):
    source_data = apps.get_model('women', 'Category')
    initial_data = [
        {'name': 'Actresses', 'slug': 'actresses'},
        {'name': 'Singers', 'slug': 'singers'}
    ]
    for data_element in initial_data:
        source_data.objects.get_or_create(**data_element)


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
