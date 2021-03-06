# Generated by Django 3.2.8 on 2021-10-17 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosMedicos',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ccMedico', models.CharField(max_length=30, unique=True, verbose_name='CcMedico')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombre', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=30, unique=True, verbose_name='Dni')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('entidad', models.CharField(max_length=50, verbose_name='Entidad')),
                ('telefono', models.CharField(max_length=45, verbose_name='Telfono')),
                ('correo', models.CharField(max_length=45, verbose_name='Correo')),
                ('enfermedades', models.CharField(max_length=256, verbose_name='Enfermedades')),
                ('alergias', models.CharField(max_length=256, verbose_name='Alergias')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriasClinicas',
            fields=[
                ('idHistoriaClinica', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAtencion', models.DateTimeField(auto_now=True)),
                ('motivoConsulta', models.CharField(max_length=256)),
                ('medicamentosFormulados', models.CharField(max_length=256)),
                ('idMedico', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='medico', to=settings.AUTH_USER_MODEL)),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='paciente', to='mediticApp.pacientes')),
            ],
        ),
    ]
