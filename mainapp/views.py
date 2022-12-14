from django.shortcuts import render,  redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.shortcuts import get_object_or_404

from .forms import BadgeAddForm
from .models import Badge

# -------------- Home page and also listing badges here ------ #
def homePageFunc(request):
	badgelist = Badge.objects.all()

	form = BadgeAddForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		messages.success(request,"Badge added successfully!")
		print("added")
	else:
		messages.error(request,"Cannot add badge!")
		print("not added")
		
	context = {"form":form,'badgelist':badgelist}
	return render(request,'index.html', context)


def registerFunc(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homeUrl")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def loginFunc(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homeUrl")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logoutFunc(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homeUrl")

def addBadgeFunc(request):
	form = BadgeAddForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		messages.success(request,"Badge added successfully!")
		return redirect('homeUrl')

	context = {"form":form}
	return render(request, "addbadge.html" ,context) 

def displayBadgeFunc(request, pkid):
	pic = get_object_or_404(Badge, id=pkid)
	context = {"pic":pic}
	return render(request, "badgedisplay.html", context)

def deleteBadgeFunc(request, pkid):
	data = get_object_or_404(Badge, id=pkid) 
	data.delete()
	return redirect('homeUrl')