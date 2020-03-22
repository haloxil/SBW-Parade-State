from django.shortcuts import render, redirect
from .models import Person
from .forms import NameForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm

# Create your views here.
def welcome(request):
	return render(request,"main/welcome.html")

def home(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return redirect("main:home")

	form = NameForm()
	persons = Person.objects.all()
	args = {"form": form, "persons": persons}
	return render(request,"main/home.html", args)

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			return redirect("main:home")

	form = NewUserForm
	return render(request,
				  "main/register.html",
				  {"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("main:home")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})

def logout_request(request):
	logout(request)
	return redirect("main:welcome")
