# Generated by Django 2.2.1 on 2019-05-13 19:07

from django.db import migrations, models


def set_sort_title_default(apps, schema_editor):
    Page = apps.get_model('wagtailcore', 'Page')
    for page in Page.objects.all():
        page.sort_title = page.title
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='sort_title',
            field=models.CharField(null=True, max_length=255, verbose_name='sorting title'),
            preserve_default=False,
        ),
        migrations.RunPython(set_sort_title_default),
        migrations.AlterField(
            model_name='page',
            name='sort_title',
            field=models.CharField(max_length=255, verbose_name='sorting title'),
            preserve_default=False,
        ),
    ]