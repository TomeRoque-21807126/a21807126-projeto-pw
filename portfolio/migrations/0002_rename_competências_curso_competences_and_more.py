# Generated by Django 4.0.6 on 2024-04-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='competências',
            new_name='competences',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='objetivos',
            new_name='objectives',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='apresentacao',
            new_name='presentation',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='nome',
            new_name='curricularUnitName',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='ano',
            new_name='curricularYear',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='semestre',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='semester',
            field=models.CharField(default='', max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='curricularIUnitReadableCode',
            field=models.CharField(max_length=13),
        ),
    ]
