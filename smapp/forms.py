from django import forms
from django.core import validators


# custom validator
def must_be_empty(value):
    if value:
        raise forms.validationError('is not empty')

# identical to creating a model
class SuggestionForm(forms.Form):
    name = forms.CharField(max_length=255) # is max len needed?
    email = forms.EmailField(max_length=255)
    verify_email = forms.EmailField(label="Please verify email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(
        required=False,
        widget = forms.HiddenInput,
        label="Leave empty",
        #validators=[validators.MaxLengthValidator(0)])
        validators=[must_be_empty],)
    """def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("Bad bot!")
        return honeypot"""

    # clean entire form
    def clean(self):
        # get ALL of the data
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if email != verify:
            raise forms.ValidationError(
                "Please enter the same email for both fields")