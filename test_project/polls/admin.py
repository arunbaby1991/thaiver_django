from django.contrib import admin

from .models import Question, Choice


# There is also a decorator for registering your ModelAdmin classes
@admin.register(Question)
class AuthorAdmin(admin.ModelAdmin):
    # To display the columns in the admin panel for questions
    list_display = ('question_text', 'weightage')


admin.site.register(Choice)