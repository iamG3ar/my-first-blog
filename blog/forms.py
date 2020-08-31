from django import forms
from .models import Post
from .models import Cv

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CvForm(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('author_name', 'address', 'phone_no', 'email_address',
        'linkedIn', 'profile', 'skills', 'projects', 'education',
        'experience', 'extra_curricular',)
