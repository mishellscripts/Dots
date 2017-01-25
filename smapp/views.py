from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms

from . import forms


def main_page(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def suggestion_view(request):
    form = forms.SuggestionForm
    # in suggestion_form, method was set to 'POST'
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        # check input, send email
        if form.is_valid():
            #print("works")
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['michelleesong@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS, 'Thank you!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})