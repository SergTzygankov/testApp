from django.contrib import admin
from .models import Test, Question, Answer, Result

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Result)
