# Generated by Django 3.0.3 on 2020-06-23 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("django_etebase", "0015_collectionitemrevision_salt"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="main_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="parent",
                to="django_etebase.CollectionItem",
            ),
        ),
        migrations.AlterUniqueTogether(name="collection", unique_together=set(),),
        migrations.RemoveField(model_name="collection", name="uid",),
        migrations.RemoveField(model_name="collection", name="version",),
    ]
