from django.contrib import admin

from .models import (Expertise, Skill)


@admin.register(Expertise)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name_expertise',)
    list_filter = ('name_expertise',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_type',)
    list_filter = ('skill_name','skill_type')

