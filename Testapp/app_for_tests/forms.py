from  django import forms

from .models import Test, Question, Answer, Result

class TestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

    class Meta:
        moddel = Test
        fields = ['name', 'description']

    class Question(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(QuestionForm, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs['class'] = 'form-control'
            self.fields['is_correct'].widget.attrs['class'] = 'form-control'
            self.fields['test'].widget.attrs['class'] = 'form-control'
            self.fields['question'].widget.attrs['class'] = 'form-control'
            self.fields['answer'].widget.attrs['class'] = 'form-control'

    class Answer(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(AnswerForm, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs['class'] = 'form-control'
            self.fields['is_correct'].widget.attrs['class'] = 'form-control'
            self.fields['question'].widget.attrs['class'] = 'form-control'
            self.fields['answer'].widget.attrs['class'] = 'form-control'

