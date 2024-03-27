from django import forms
from .models import Test, Question, Answer

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']


AnswerFormSet = forms.inlineformset_factory(
    Question,  # Родительская модель
    Answer,    # Дочерняя модель
    fields=['text', 'is_correct'],  # Поля, которые вы хотите отобразить в форме
    extra=4,   # Изначальное количество дополнительных форм
    can_delete=True,  # Позволяет удалять дополнительные формы
)
