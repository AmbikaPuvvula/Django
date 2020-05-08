from django.shortcuts import render
from userApp.forms import UsersignupForm,DetailsForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Details
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request,pk):
	data = User.objects.get(id=pk)
	if request.method == 'POST':
		form = DetailsForm(request.POST,request.FILES)
		print("Iam")
		if form.is_valid():
			print('Iam here'+ str(pk) +' '+request.POST['phoneNo'])
			try:
				f=form.save(commit=False)
				f.user_id = data.id
				f.save()
				return HttpResponse("Done.....")
			except:
				return HttpResponse("Something went Wrong")
	form = DetailsForm()
	return render(request,'userApp/profile.html',{'form':form,'data':data})