from django import forms
from datetime import datetime
from django.utils import timezone

from users.models import User 
from .models import ROLE_CHOICES, Comment, Notification, Task, TaskList, Membership, Tags, TaskGroup


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
            queryset=Tags.objects.filter(status='Active'),
            widget=forms.CheckboxSelectMultiple,
            required=False)
            
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'estimation', 'assignee', 'status', 'priority', 'tags']
        widgets = {
            'deadline': forms.DateInput(attrs={'type':'datetime-local'})
        }

class TaskListForm(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = ['name', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type':'datetime-local'})
        }
        
class NotificationGroupForm(forms.Form):
    ROLE_CHOICES = [
         ('', '---------'),
        ('Moderators', 'Moderators'),
        ('Members', 'Members'),
    ]
    users = forms.ChoiceField(choices=ROLE_CHOICES)
    message = forms.CharField(max_length=2048, widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(NotificationGroupForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['message'].widget.attrs['cols'] = 50
        self.fields['message'].widget.attrs['rows'] = 5
        self.fields['users'].widget.attrs['style'] = 'width:150px;'

class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tags
        fields = '__all__'

class MembershipForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    message = forms.CharField(max_length=2048, widget=forms.Textarea, required=False)

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'4',
    }))

    class Meta:
        model = Comment 
        fields = ['content']