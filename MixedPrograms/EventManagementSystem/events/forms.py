from django import forms
from .models import Comment, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("user", )

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['title', 'subtitle', 'description', 'time', 'place', 'tickets_amount', 'price']
        widgets={'time': forms.DateInput(attrs={'type': 'date'})}
