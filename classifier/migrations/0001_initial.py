# Generated by Django 3.2 on 2023-11-16 16:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'aeroplane'), (2, 'car'), (3, 'bird'), (4, 'cat'), (5, 'deer'), (6, 'dog'), (7, 'frog'), (8, 'horse'), (9, 'ship'), (10, 'fish')], primary_key=True, serialize=False)),
                ('category_description', models.CharField(choices=[(1, 'aeroplane'), (2, 'car'), (3, 'bird'), (4, 'cat'), (5, 'deer'), (6, 'dog'), (7, 'frog'), (8, 'horse'), (9, 'ship'), (10, 'fish')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'Red'), (2, 'Orange'), (3, 'Yellow'), (4, 'Green'), (5, 'Blue'), (6, 'Indigo'), (7, 'Violet')], primary_key=True, serialize=False)),
                ('color_description', models.CharField(choices=[(1, 'Red'), (2, 'Orange'), (3, 'Yellow'), (4, 'Green'), (5, 'Blue'), (6, 'Indigo'), (7, 'Violet')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.color')),
                ('image_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.image')),
            ],
        ),
    ]
