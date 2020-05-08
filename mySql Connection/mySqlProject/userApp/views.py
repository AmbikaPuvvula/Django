from django.shortcuts import render
from userApp.forms import UsersignupForm
from django.http import HttpResponse

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = UsersignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Done")
	form = UsersignupForm()
	return render(request,'userApp/signup.html',{'form':form})


def home(request):
	return render(request,'userApp/home.html')
