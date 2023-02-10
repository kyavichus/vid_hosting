from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from video_hosting.models import Video


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ModuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



    class Meta:
        model = Video
        fields = ['title', 'category', 'description', 'image', 'file']
