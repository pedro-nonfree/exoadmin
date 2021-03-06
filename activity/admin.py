from django.contrib import admin

from django.utils.translation import gettext as _

from . import models

@admin.register(models.Expense_type)
class Expense_type_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(models.Expense)
class Expense(admin.ModelAdmin):
    list_display = ('activity', 'expense_type', 'cost', 'comments', 'date',)

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('activity', 'task_type', 'identity', 'time', 'comments', 'date',)

class ExpenseInline(admin.TabularInline):
    model = models.Expense
    extra = 0

class TaskInline(admin.TabularInline):
    model = models.Task
    extra = 0
    raw_id_fields = ('identity',)

@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

def update_counters(self, request, queryset):
    for obj in queryset:
        obj.save()
    self.message_user(request, _('Counters updated'))
update_counters.short_description = _('Update time and cost counters')

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = (TaskInline, ExpenseInline,)
    readonly_fields = ('count_time', 'count_cost',)
    list_display = ('title', 'activity_type', 'count_time', 'count_cost')
    search_fields = ('title',)
    actions = (update_counters,)
