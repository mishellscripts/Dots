from django import forms

from . import models


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea
                                #(attrs={'style': 'font-size: 1.5em'}),
                           ,label='',
                           )
    text.widget.attrs.update({'class': 'form_input'})

    class Meta:
        model = models.Post
        fields = ['text', ]

    def clean(self):
        # get ALL of the data
        cleaned_data = super().clean()
        text = cleaned_data['text']

        # SECURITY CHECK HERE
