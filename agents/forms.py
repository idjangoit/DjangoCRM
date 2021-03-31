from django import forms
from leads.models import Agent


class AgentModelForm(forms.Form):
    model = Agent
    fields = (
        'user',
        )