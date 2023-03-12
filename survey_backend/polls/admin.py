from django.contrib import admin

from .models import Question, Choice, Point


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'pub_date',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Point)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'points',)
    search_fields = ('user',)
    list_filter = ('points',)
