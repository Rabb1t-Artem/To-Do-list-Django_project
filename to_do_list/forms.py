from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model

from to_do_list.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3}),
            "deadline": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }
