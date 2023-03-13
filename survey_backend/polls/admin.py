from django.contrib import admin

from .models import Poll, Question, Choice, Point


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll', 'text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'poll',)
    search_fields = ('text',)
    empty_value_display = '-пусто-'


@admin.register(Point)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'question',)
    search_fields = ('user',)
    list_filter = ('user',)
