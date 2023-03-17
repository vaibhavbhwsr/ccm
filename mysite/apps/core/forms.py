from django import forms
from core.models import Case
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class NewCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'detail', 'number', 'case_type', 'case_status', 'opened_at', 'lawyer', 'client']
        widgets = {
            'opened_at': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        query_lawyer = User.objects.filter(user_info__user_type="Lawyer")
        query_client = User.objects.filter(user_info__user_type="Client")
        self.fields['lawyer'].queryset = query_lawyer
        self.fields['client'].queryset = query_client
