from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = fields
        fields = ('first_name', 'last_name','L1_manager','data_of_joining')
