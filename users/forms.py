from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	fullname = forms.CharField()
	email = forms.EmailField()
	address = forms.CharField(required=False)
	city = forms.CharField(required=False)
	state = forms.CharField(required=False)
	country = forms.CharField(required=False)
	pincode = forms.CharField(max_length=6)

	class Meta:
		model = User
		fields = ['fullname','email','username','address', 'city','state','country','pincode','password1', 'password2']