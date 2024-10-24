from django import forms
from tweet.models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Tweetform(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ["text","Photo"]
        
class userRegistarionForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")