from django import forms
from .models import Comment

class commentForm(forms.ModelForm):
    class Meta():
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name"
        }

