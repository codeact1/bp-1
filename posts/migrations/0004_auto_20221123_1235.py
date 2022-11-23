# Generated by Django 4.1.3 on 2022-11-23 12:13

from django.db import migrations

def populate_status(apps, schemaeditor):
    statuses = {
        "published" : "A post that has been published for all to view.",
        "draft" : "A post that not has yet been published.",
    }
    Status = apps.get_model("posts", "Status")
    for name, desc in statuses.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_status_post_status'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]

