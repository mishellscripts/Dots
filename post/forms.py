from django import forms

from . import models


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = models.Post
        fields = ['text', ]

    def clean(self):
        # get ALL of the data
        cleaned_data = super().clean()
        text = cleaned_data['text']

        # SECURITY CHECK HERE
