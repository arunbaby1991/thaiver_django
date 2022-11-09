from django.contrib import admin

from .models import Question, Choice


# The admin interface has the ability to edit models on the same page as a parent model.
class ChoiceInline(admin.TabularInline):
    model = Choice


# There is also a decorator for registering your ModelAdmin classes
@admin.register(Question)
class AuthorAdmin(admin.ModelAdmin):
    # To display the columns in the admin panel for questions
    list_display = ('question_text', 'weightage')

    # Once click on + sign for choice we can add question and choice in the same page
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Choice)