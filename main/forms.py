from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .choices import *

class NameForm(forms.ModelForm):

	rank = forms.ChoiceField(choices=rank_choice)
	status = forms.ChoiceField(choices=status_choice)

	class Meta:
		model = Person
		fields = ["rank", "status"]


class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "password1", "password2")