from django.contrib import admin

from QuestionApp.models import Choice, Question, Vote

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInLine]
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

class ReadOnlyMixin:
    def has_add_permission(self, request):
        return False
'''
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
'''
class VoteAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ('voter_name', 'vote_date', 'choice')


admin.site.register(Vote, VoteAdmin)