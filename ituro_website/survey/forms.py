from django import forms
from survey.models import Survey, TextQuestion, TextAreaQuestion, ChoiceQuestion


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ["participant"]

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.initial["participant"] = ""
        questions = []
        for text_question in self.instance.textquestion_set.all():
            questions.append(text_question)
        for textarea_question in self.instance.textareaquestion_set.all():
            questions.append(textarea_question)
        for multiplechoice_question in self.instance.choicequestion_set.all():
            questions.append(multiplechoice_question)
        questions.sort(key=lambda e : e.order)
        for question in questions:
            if isinstance(question, TextQuestion):
                self.fields[question.question] = forms.CharField(max_length=200)
            elif isinstance(question, TextAreaQuestion):
                self.fields[question.question] = forms.CharField(widget=forms.Textarea)
            elif isinstance(question, ChoiceQuestion):
                choices = []
                for choice in question.choices.all():
                    choices.append((str(choice.answer), str(choice.answer).capitalize()))
                if question.is_multiple:
                    self.fields[question.question] = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
                else:
                    self.fields[question.question] = forms.ChoiceField(choices=choices, widget=forms.Select)
