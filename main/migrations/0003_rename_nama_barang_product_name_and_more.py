# Generated by Django 5.1.1 on 2024-09-15 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_delete_moodentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nama_barang',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nama_mahasiswa',
        ),
    ]