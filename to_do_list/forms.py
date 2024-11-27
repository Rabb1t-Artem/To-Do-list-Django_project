from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model

from to_do_list.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    tags = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
