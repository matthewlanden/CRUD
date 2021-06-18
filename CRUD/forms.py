from django import forms





from .models import Task


class TaskForm(forms.ModelForm):
    
    
    class Meta:

        model   = Task
        fields  = ['task', 'complete']
        widgets = {
            'task'     : forms.TextInput(attrs={'placeholder' : 'Enter Your Task Here :'}),
            'complete' : forms.CheckboxInput(attrs={})
        }
        