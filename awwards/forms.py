from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Posts,Comments,Likes
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']
        # fields = ['']

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']
        fields = ['name','link','image1','image2','image3','video']

class Comments(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = []
        fields = ['comment']


rates_choices = [
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
]

class Votes(forms.Form):
    design = forms.CharField(label='Design level', widget=forms.RadioSelect(choices=rates_choices))

    usability = forms.CharField(label='Usability level', widget=forms.RadioSelect(choices=rates_choices))

    creativity  = forms.CharField(label='Creativity level', widget=forms.RadioSelect(choices=rates_choices))

    content = forms.CharField(label='Content level', widget=forms.RadioSelect(choices=rates_choices))
