# Generated by Django 4.0.6 on 2024-05-30 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='albuns/capas/')),
                ('data_lancamento', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='bandas/fotos/')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('pais_origem', models.CharField(blank=True, max_length=50, null=True)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('data_formacao', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('duracao', models.DurationField(blank=True, null=True)),
                ('spotify_link', models.URLField(blank=True, null=True)),
                ('letra', models.TextField(blank=True, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='bandas.banda'),
        ),
    ]
