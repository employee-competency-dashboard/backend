# Generated by Django 4.2 on 2024-10-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_skills', '0002_employee_skills_alter_employee_grade_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('last_name',), 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='expertise',
            name='name_expertise',
            field=models.CharField(choices=[('Development Competency', 'Компетенция Разработка'), ('Testing Competency', 'Компетнция Тестирование'), ('Design Competency', 'Компетнция Дизайн'), ('Project Management Methodologies', 'Методологии управления проектами'), ('Public Speaking Skills', 'Навыки публичных выступлений'), ('Organization of Workflow', 'Организация рабочего процесса'), ('Interface Design', 'Проектирование интерфейсов')], max_length=64, verbose_name='Название компетенции'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(choices=[('django', 'Django'), ('python', 'Python'), ('api', 'API'), ('tax_reporting', 'Налоговая отчетность'), ('financial_accounting', 'Бухгалтерский учёт')], max_length=32, verbose_name='Название навыка'),
        ),
    ]